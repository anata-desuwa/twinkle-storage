import json, os, glob, re

d = os.path.dirname(__file__)
with open(os.path.join(d, "tsk_character_name.json"), encoding="utf-8") as f:
    name_map = json.load(f)

# Intentional names that should not be looked up
skip_names = {"unk", "？", "？？", "？？？", "？？？？", "？？？？？", "？？？？？？", "ＸＥＬＯＳ"}

pat = re.compile(r'^speaker\s*=\s*"(.+)"')

toml_files = glob.glob(os.path.join(d, "translations", "*.toml"))
total = len(toml_files)

for i, filepath in enumerate(toml_files):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines(keepends=True)
    new_lines = []
    changed = False

    for line in lines:
        m = pat.match(line)
        if m:
            name = m.group(1)
            if name in skip_names or name not in name_map:
                new_lines.append(line)
            else:
                new_lines.append(f'speaker_original = "{name}"\nspeaker_translation = "{name_map[name]}"\n')
                changed = True
        else:
            new_lines.append(line)

    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

    if (i + 1) % 200 == 0 or i == total - 1:
        print(f"Processed {i + 1}/{total} files")

print("Done!")
