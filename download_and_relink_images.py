import os
import re
import requests
import glob
from PIL import Image
import tempfile

def get_image_dimensions(image_path):
    """Get width and height of an image."""
    try:
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

def clean_media_files(folder_path):
    """Remove all existing image and video files from the folder."""
    media_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.bmp', '.tiff', '.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mkv']
    
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file.lower())
            if ext in media_extensions:
                try:
                    os.remove(file_path)
                    print(f"Removed existing file: {file}")
                except Exception as e:
                    print(f"Could not remove {file}: {e}")

def find_all_md_files(root_dir):
    """Find all markdown files in the directory and subdirectories."""
    md_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def process_markdown_file(md_path):
    """Process a single markdown file."""
    print(f"\nProcessing: {md_path}")
    
    img_folder = os.path.dirname(md_path)
    
    # Clean existing media files
    clean_media_files(img_folder)
    
    # Get the relative path from the repo root
    repo_root = os.path.abspath(os.getcwd())
    abs_md_folder = os.path.abspath(img_folder)
    rel_folder = os.path.relpath(abs_md_folder, repo_root).replace("\\", "/")

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern to match both markdown images and HTML img/video tags with remote URLs
    img_pattern = re.compile(r'!\[([^\]]*)\]\((https?://[^\)]+)\)')
    html_img_pattern = re.compile(r'<img[^>]*src=["\']([^"\']*https?://[^"\']*)["\'][^>]*>')
    video_pattern = re.compile(r'<video[^>]*src=["\']([^"\']*https?://[^"\']*)["\'][^>]*>')
    
    # Find all matches
    md_matches = img_pattern.findall(content)
    html_img_matches = html_img_pattern.findall(content)
    video_matches = video_pattern.findall(content)
    
    if not md_matches and not html_img_matches and not video_matches:
        print("No remote images or videos found.")
        return

    # Process markdown images
    for idx, (alt, url) in enumerate(md_matches, 1):
        ext = os.path.splitext(url)[1].split("?")[0] or ".png"
        local_name = f"image{idx}{ext}"
        local_path = os.path.join(img_folder, local_name)
        cdn_url = f"https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/{rel_folder}/{local_name}"
        
        try:
            resp = requests.get(url)
            resp.raise_for_status()
            with open(local_path, "wb") as img_file:
                img_file.write(resp.content)
            print(f"Downloaded {url} -> {local_name}")
            
            # Get image dimensions
            width, height = get_image_dimensions(local_path)
            width_attr = f'width="{width}"' if width else 'width="800"'
            height_attr = f'height="{height}"' if height else 'height="600"'
            
            # Replace markdown notation with HTML notation
            old_pattern = re.escape(f'![{alt}]({url})')
            new_html = f'<img src="{cdn_url}" alt="{alt}" {width_attr} {height_attr}>'
            content = re.sub(old_pattern, new_html, content)
            
        except Exception as e:
            print(f"Failed to download {url}: {e}")

    # Process HTML images
    img_counter = len(md_matches) + 1
    for url in html_img_matches:
        ext = os.path.splitext(url)[1].split("?")[0] or ".png"
        local_name = f"image{img_counter}{ext}"
        local_path = os.path.join(img_folder, local_name)
        cdn_url = f"https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/{rel_folder}/{local_name}"
        
        try:
            resp = requests.get(url)
            resp.raise_for_status()
            with open(local_path, "wb") as img_file:
                img_file.write(resp.content)
            print(f"Downloaded {url} -> {local_name}")
            
            # Get image dimensions
            width, height = get_image_dimensions(local_path)
            width_attr = f'width="{width}"' if width else 'width="800"'
            height_attr = f'height="{height}"' if height else 'height="600"'
            
            # Replace the src URL and ensure proper width/height attributes
            old_img_pattern = re.compile(r'<img[^>]*src=["\']' + re.escape(url) + r'["\'][^>]*>')
            
            def replace_img_tag(match):
                img_tag = match.group(0)
                # Extract alt text if present
                alt_match = re.search(r'alt=["\']([^"\']*)["\']', img_tag)
                alt_text = alt_match.group(1) if alt_match else ""
                return f'<img src="{cdn_url}" alt="{alt_text}" {width_attr} {height_attr}>'
            
            content = old_img_pattern.sub(replace_img_tag, content)
            img_counter += 1
            
        except Exception as e:
            print(f"Failed to download {url}: {e}")

    # Process videos
    video_counter = 1
    for url in video_matches:
        ext = os.path.splitext(url)[1].split("?")[0] or ".mp4"
        local_name = f"video{video_counter}{ext}"
        local_path = os.path.join(img_folder, local_name)
        cdn_url = f"https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/{rel_folder}/{local_name}"
        
        try:
            resp = requests.get(url)
            resp.raise_for_status()
            with open(local_path, "wb") as video_file:
                video_file.write(resp.content)
            print(f"Downloaded {url} -> {local_name}")
            
            # Get video dimensions
            width, height = get_video_dimensions(local_path)
            width_attr = f'width="{width}"'
            height_attr = f'height="{height}"'
            
            # Replace the src URL and ensure proper width/height attributes
            old_video_pattern = re.compile(r'<video[^>]*src=["\']' + re.escape(url) + r'["\'][^>]*>')
            
            def replace_video_tag(match):
                video_tag = match.group(0)
                # Preserve existing attributes like controls, autoplay, muted
                controls = 'controls' if 'controls' in video_tag else ''
                autoplay = 'autoplay' if 'autoplay' in video_tag else ''
                muted = 'muted' if 'muted' in video_tag else ''
                loop = 'loop' if 'loop' in video_tag else ''
                
                attributes = ' '.join(filter(None, [controls, autoplay, muted, loop]))
                return f'<video src="{cdn_url}" {width_attr} {height_attr} {attributes}></video>'
            
            content = old_video_pattern.sub(replace_video_tag, content)
            video_counter += 1
            
        except Exception as e:
            print(f"Failed to download {url}: {e}")

    # Save the updated content
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Completed processing: {md_path}")

def main():
    user_input = input("Enter the path to the markdown file or 'all' to process all markdown files: ").strip()
    
    if user_input.lower() == 'all':
        # Process all markdown files
        repo_root = os.path.abspath(os.getcwd())
        md_files = find_all_md_files(repo_root)
        
        if not md_files:
            print("No markdown files found.")
            return
        
        print(f"Found {len(md_files)} markdown files:")
        for md_file in md_files:
            print(f"  {md_file}")
        
        confirm = input(f"\nDo you want to process all {len(md_files)} files? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Operation cancelled.")
            return
        
        for md_file in md_files:
            try:
                process_markdown_file(md_file)
            except Exception as e:
                print(f"Error processing {md_file}: {e}")
                continue
        
        print(f"\nCompleted processing all {len(md_files)} markdown files.")
    
    else:
        # Process single file
        md_path = user_input
        if not os.path.isfile(md_path):
            print("File not found.")
            return
        
        process_markdown_file(md_path)

    print("Done. All images and videos downloaded and links updated to HTML notation with dimensions.")

if __name__ == "__main__":
    main()