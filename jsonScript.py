import os
import yaml
import json
import re

def _extract_frontmatter_yaml(content: str):
    # Support standard YAML frontmatter:
    # ---
    # key: value
    # ---
    if content.startswith('\ufeff'):
        content = content.lstrip('\ufeff')
    if not content.startswith('---'):
        return None

    lines = content.splitlines()
    if not lines or lines[0].strip() != '---':
        return None

    end_index = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_index = i
            break

    if end_index is None:
        return None

    fm = "\n".join(lines[1:end_index]).strip()
    if not fm:
        return None

    return yaml.safe_load(fm)

def _extract_legacy_html_comment_yaml(content: str):
    # Legacy format currently used in this repo:
    # <!--
    # title: "..."
    # ...
    # -->
    start = content.find('<!--')
    end = content.find('-->', start)
    if start == -1 or end == -1:
        return None
    metadata_content = content[start + 4:end].strip()
    if not metadata_content:
        return None
    return yaml.safe_load(metadata_content)

def extract_metadata(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    metadata = _extract_frontmatter_yaml(content) or _extract_legacy_html_comment_yaml(content)
    if not metadata:
        return None

    # Normalize expected fields (keep backward compatibility with existing JSON consumers)
    if 'updatedAt' not in metadata and 'createdAt' in metadata:
        metadata['updatedAt'] = metadata['createdAt']

    return metadata

def construct_url(base_url, filepath):
    relative_path = os.path.relpath(filepath, start=root_dir).replace(os.sep, '/').lstrip("./")
    return f"{base_url}/{relative_path}"

root_dir = '.'
base_url = 'https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials'
all_metadata = []

for root, dirs, files in os.walk(root_dir):
    files.sort()
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            metadata = extract_metadata(filepath)
            if metadata:
                metadata['url'] = construct_url(base_url, filepath)
                metadata['id'] = re.sub(r'-+', '-', re.sub(r'[^a-z0-9\-]', '-', metadata['title'].lower())).strip('-')
                all_metadata.append(metadata)

# Sort by createdAt (ascending order)
all_metadata.sort(key=lambda x: x.get('createdAt', ''))

with open('metadata.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_metadata, json_file, indent=4, ensure_ascii=False)
