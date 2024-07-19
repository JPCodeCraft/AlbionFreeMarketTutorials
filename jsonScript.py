import os
import yaml
import json

def extract_metadata(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read().split('---')
        if len(content) >= 3:
            metadata = yaml.safe_load(content[1])
            return metadata
    return None

def construct_url(base_url, filepath):
    relative_path = os.path.relpath(filepath, start=root_dir).replace(os.sep, '/').lstrip("./")
    return f"{base_url}/{relative_path}"

root_dir = '.'
base_url = 'https://raw.githubusercontent.com/JPCodeCraft/AlbionFreeMarketTutorials/main'
all_metadata = []

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            metadata = extract_metadata(filepath)
            if metadata:
                metadata['url'] = construct_url(base_url, filepath)
                metadata['id'] = metadata['title'].replace(' ', '-').lower()
                all_metadata.append(metadata)

with open('metadata.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_metadata, json_file, indent=4, ensure_ascii=False)