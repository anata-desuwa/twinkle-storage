import json
import os
import re
import glob

json_path = os.path.join(os.path.dirname(__file__), "tsk_character_name.json")
translations_dir = os.path.join(os.path.dirname(__file__), "translations")

with open(json_path, "r", encoding="utf-8") as f:
    name_map = json.load(f)

pattern = re.compile(r'^(speaker\s*=\s*")(.+)(".*)$')

toml_files = glob.glob(os.path.join(translations_dir, "*.toml"))
total = len(toml_files)

for i, filepath in enumerate(toml_files):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    changed = False
    new_lines = []
    for line in lines:
        m = pattern.match(line)
        if m:
            prefix = m.group(1)
            name = m.group(2)
            suffix = m.group(3)
            if name in name_map:
                line = f'{prefix}{name_map[name]}{suffix}\n'
                changed = True
        new_lines.append(line)

    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

    if (i + 1) % 200 == 0 or i == total - 1:
        print(f"Processed {i + 1}/{total} files")

print("Done!")
