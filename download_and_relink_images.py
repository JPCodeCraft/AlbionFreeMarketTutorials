import os
import re
import requests

def main():
    md_path = input("Enter the path to the markdown file: ").strip()
    if not os.path.isfile(md_path):
        print("File not found.")
        return

    img_folder = os.path.dirname(md_path)
    # Get the relative path from the repo root
    repo_root = os.path.abspath(os.getcwd())
    abs_md_folder = os.path.abspath(img_folder)
    rel_folder = os.path.relpath(abs_md_folder, repo_root).replace("\\", "/")

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    img_pattern = re.compile(r'!\[([^\]]*)\]\((https?://[^\)]+)\)')
    matches = img_pattern.findall(content)

    if not matches:
        print("No remote images found.")
        return

    for idx, (alt, url) in enumerate(matches, 1):
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
            # Replace only the specific image link
            content = re.sub(
                re.escape(f"]({url})"),
                f"]({cdn_url})",
                content,
                count=1
            )
        except Exception as e:
            print(f"Failed to download {url}: {e}")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("Done. All images downloaded and links updated.")

if __name__ == "__main__":
    main()