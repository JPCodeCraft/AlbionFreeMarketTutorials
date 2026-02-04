import os
import re
import requests
import glob
from PIL import Image
import tempfile
import sys
import hashlib
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

MEDIA_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.bmp', '.tiff', '.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mkv']

def get_image_dimensions(image_path):
    """Get width and height of an image."""
    try:
        ext = os.path.splitext(image_path)[1].lower()
        if ext == ".svg":
            with open(image_path, "rb") as f:
                svg = ET.fromstring(f.read())
            w = svg.get("width")
            h = svg.get("height")
            viewbox = svg.get("viewBox")
            if (not w or not h) and viewbox:
                _, _, vw, vh = map(float, viewbox.strip().split())
                return int(vw), int(vh)
            if w and h:
                return int(float(w)), int(float(h))
            return None, None

        with Image.open(image_path) as img:
            return img.size  # returns (width, height)
    except Exception as e:
        print(f"Could not get dimensions for {image_path}: {e}")
        return None, None

def get_video_dimensions(video_path):
    """Get width and height of a video. Returns default dimensions if unable to determine."""
    try:
        import cv2
        cap = cv2.VideoCapture(video_path)
        if cap.isOpened():
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            cap.release()
            return width, height
        return 800, 600  # default dimensions
    except ImportError:
        print("OpenCV not available for video dimension detection. Using default 800x600.")
        return 800, 600
    except Exception as e:
        print(f"Could not get video dimensions for {video_path}: {e}")
        return 800, 600

def find_all_md_files(root_dir):
    """Find all markdown files in the directory and subdirectories."""
    md_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def is_cdn_url(url):
    return url.startswith("https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/")

def content_hash_name(content, ext, prefix):
    content_hash = hashlib.sha256(content).hexdigest()[:12]
    ext = ext or ".png"
    if not ext.startswith("."):
        ext = f".{ext}"
    return f"{prefix}_{content_hash}{ext}"

def replace_one(match_text, replacement, content):
    return content.replace(match_text, replacement, 1)

def extract_referenced_media(content):
    img_pattern = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')
    html_img_pattern = re.compile(r'<img[^>]*\ssrc=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)
    video_pattern = re.compile(r'<video[^>]*\ssrc=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)
    source_pattern = re.compile(r'<source[^>]*\ssrc=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)

    urls = []
    urls += img_pattern.findall(content)
    urls += html_img_pattern.findall(content)
    urls += video_pattern.findall(content)
    urls += source_pattern.findall(content)

    basenames = set()
    for url in urls:
        path = urlparse(url).path
        basename = os.path.basename(path)
        if not basename:
            continue
        _, ext = os.path.splitext(basename.lower())
        if ext in MEDIA_EXTENSIONS:
            basenames.add(basename)
    return basenames

def collect_referenced_media_in_folder(folder_path):
    referenced = set()
    for name in os.listdir(folder_path):
        if not name.lower().endswith('.md'):
            continue
        md_path = os.path.join(folder_path, name)
        try:
            with open(md_path, "r", encoding="utf-8") as f:
                referenced.update(extract_referenced_media(f.read()))
        except Exception as e:
            print(f"Could not read {md_path}: {e}")
    return referenced

def prune_media_files(folder_path, referenced_files):
    for name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, name)
        if not os.path.isfile(file_path):
            continue
        _, ext = os.path.splitext(name.lower())
        if ext in MEDIA_EXTENSIONS and name not in referenced_files:
            try:
                os.remove(file_path)
                print(f"Pruned unreferenced file: {name}")
            except Exception as e:
                print(f"Could not remove {name}: {e}")

def process_markdown_file(md_path, rebuild_cdn=False):
    """Process a single markdown file."""
    print(f"\nProcessing: {md_path}")
    
    img_folder = os.path.dirname(md_path)
    
    # Get the relative path from the repo root
    repo_root = os.path.abspath(os.getcwd())
    abs_md_folder = os.path.abspath(img_folder)
    rel_folder = os.path.relpath(abs_md_folder, repo_root).replace("\\", "/")

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern to match both markdown images and HTML img/video tags with remote URLs
    img_pattern = re.compile(r'!\[([^\]]*)\]\((https?://[^\)]+)\)')
    html_img_pattern = re.compile(r'(<img[^>]*src=["\']([^"\']*https?://[^"\']*)["\'][^>]*>)')
    video_pattern = re.compile(r'(<video[^>]*src=["\']([^"\']*https?://[^"\']*)["\'][^>]*>.*?</video>)', re.DOTALL)
    
    # Find all matches
    md_matches = img_pattern.findall(content)
    html_img_matches = html_img_pattern.findall(content)
    video_matches = video_pattern.findall(content)
    
    if not md_matches and not html_img_matches and not video_matches:
        print("No remote images or videos found.")
        return

    # Process markdown images
    for idx, (alt, url) in enumerate(md_matches, 1):
        if is_cdn_url(url) and not rebuild_cdn:
            continue
        try:
            resp = requests.get(url)
            resp.raise_for_status()
            content_bytes = resp.content
            ext = os.path.splitext(urlparse(url).path)[1] or ".png"
            local_name = content_hash_name(content_bytes, ext, "image")
            local_path = os.path.join(img_folder, local_name)
            cdn_url = f"https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/{rel_folder}/{local_name}"
            with open(local_path, "wb") as img_file:
                img_file.write(content_bytes)
            print(f"Downloaded {url} -> {local_name}")
            
            # Get image dimensions
            width, height = get_image_dimensions(local_path)
            width_attr = f'width="{width}"' if width else 'width="800"'
            height_attr = f'height="{height}"' if height else 'height="600"'
            
            # Replace markdown notation with HTML notation
            old_text = f'![{alt}]({url})'
            new_html = f'<img src="{cdn_url}" alt="{alt}" {width_attr} {height_attr}>'
            content = replace_one(old_text, new_html, content)
            
        except Exception as e:
            print(f"Failed to download {url}: {e}")

    # Process HTML images
    img_counter = len(md_matches) + 1
    for full_tag, url in html_img_matches:
        if is_cdn_url(url) and not rebuild_cdn:
            continue
        try:
            resp = requests.get(url)
            resp.raise_for_status()
            content_bytes = resp.content
            ext = os.path.splitext(urlparse(url).path)[1] or ".png"
            local_name = content_hash_name(content_bytes, ext, "image")
            local_path = os.path.join(img_folder, local_name)
            cdn_url = f"https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/{rel_folder}/{local_name}"
            with open(local_path, "wb") as img_file:
                img_file.write(content_bytes)
            print(f"Downloaded {url} -> {local_name}")
            
            # Get image dimensions
            width, height = get_image_dimensions(local_path)
            width_attr = f'width="{width}"' if width else 'width="800"'
            height_attr = f'height="{height}"' if height else 'height="600"'
            
            # Replace the src URL and ensure proper width/height attributes
            alt_match = re.search(r'alt=["\']([^"\']*)["\']', full_tag)
            alt_text = alt_match.group(1) if alt_match else ""
            new_tag = f'<img src="{cdn_url}" alt="{alt_text}" {width_attr} {height_attr}>'
            content = replace_one(full_tag, new_tag, content)
            img_counter += 1
            
        except Exception as e:
            print(f"Failed to download {url}: {e}")

    # Process videos
    video_counter = 1
    for full_tag, url in video_matches:
        if is_cdn_url(url) and not rebuild_cdn:
            continue
        try:
            resp = requests.get(url)
            resp.raise_for_status()
            content_bytes = resp.content
            ext = os.path.splitext(urlparse(url).path)[1] or ".mp4"
            local_name = content_hash_name(content_bytes, ext, "video")
            local_path = os.path.join(img_folder, local_name)
            cdn_url = f"https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/{rel_folder}/{local_name}"
            with open(local_path, "wb") as video_file:
                video_file.write(content_bytes)
            print(f"Downloaded {url} -> {local_name}")
            
            # Get video dimensions
            width, height = get_video_dimensions(local_path)
            width_attr = f'width="{width}"'
            height_attr = f'height="{height}"'
            
            # Replace the src URL and ensure proper width/height attributes
            # Preserve existing attributes like controls, autoplay, muted
            controls = 'controls' if 'controls' in full_tag else ''
            autoplay = 'autoplay' if 'autoplay' in full_tag else ''
            muted = 'muted' if 'muted' in full_tag else ''
            loop = 'loop' if 'loop' in full_tag else ''
            attributes = ' '.join(filter(None, [controls, autoplay, muted, loop]))
            new_tag = f'<video src="{cdn_url}" {width_attr} {height_attr} {attributes}></video>'
            content = replace_one(full_tag, new_tag, content)
            video_counter += 1
            
        except Exception as e:
            print(f"Failed to download {url}: {e}")

    # Save the updated content
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Completed processing: {md_path}")

def parse_args(argv):
    rebuild_cdn = False
    prune = True
    path_arg = None
    for arg in argv[1:]:
        if arg == "--rebuild-cdn":
            rebuild_cdn = True
        elif arg == "--no-prune":
            prune = False
        else:
            path_arg = arg
    return path_arg, rebuild_cdn, prune

def main():
    # Prefer CLI arg if provided; fall back to interactive prompt.
    path_arg, rebuild_cdn, prune = parse_args(sys.argv)
    cli_mode = path_arg is not None
    if cli_mode:
        user_input = path_arg.strip()
    else:
        try:
            user_input = input("Enter the path to the markdown file or 'all' to process all markdown files: ").strip()
        except EOFError:
            user_input = 'all'

    if user_input.lower() == 'all':
        # Process all markdown files
        repo_root = os.path.abspath(os.getcwd())
        md_files = find_all_md_files(repo_root)

        if not md_files:
            print("No markdown files found.")
            return

        if not cli_mode:
            print(f"Found {len(md_files)} markdown files:")
            for md_file in md_files:
                print(f"  {md_file}")

            confirm = input(f"\nDo you want to process all {len(md_files)} files? (y/n): ").strip().lower()
            if confirm != 'y':
                print("Operation cancelled.")
                return
        
        for md_file in md_files:
            try:
                process_markdown_file(md_file, rebuild_cdn=rebuild_cdn)
            except Exception as e:
                print(f"Error processing {md_file}: {e}")
                continue

        if prune:
            folders = sorted({os.path.dirname(p) for p in md_files})
            for folder in folders:
                referenced = collect_referenced_media_in_folder(folder)
                prune_media_files(folder, referenced)
        
        print(f"\nCompleted processing all {len(md_files)} markdown files.")
    
    else:
        # Process single file
        md_path = user_input
        if not os.path.isfile(md_path):
            print("File not found.")
            return
        
        process_markdown_file(md_path, rebuild_cdn=rebuild_cdn)
        if prune:
            folder = os.path.dirname(md_path)
            referenced = collect_referenced_media_in_folder(folder)
            prune_media_files(folder, referenced)

    print("Done. All images and videos downloaded and links updated to HTML notation with dimensions.")

if __name__ == "__main__":
    main()
