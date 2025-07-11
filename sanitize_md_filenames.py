import os
import re

def sanitize_filename(filename):
    # Lowercase, replace spaces with dashes, remove special chars except dash/underscore/dot
    name, ext = os.path.splitext(filename)
    name = name.lower()
    name = name.replace(' ', '-')
    name = re.sub(r'[^a-z0-9\-_\.]', '', name)
    return name + ext

def sanitize_md_files(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            if fname.lower().endswith('.md'):
                sanitized = sanitize_filename(fname)
                if fname != sanitized:
                    src = os.path.join(dirpath, fname)
                    dst = os.path.join(dirpath, sanitized)
                    # Avoid overwriting existing files
                    if not os.path.exists(dst):
                        print(f"Renaming: {src} -> {dst}")
                        os.rename(src, dst)
                    else:
                        print(f"Skipped (target exists): {dst}")

if __name__ == "__main__":
    # Change '.' to the root directory you want to scan
    sanitize_md_files(".")