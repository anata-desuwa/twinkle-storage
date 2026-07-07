import json, os, glob, re

d = os.path.dirname(__file__)
with open(os.path.join(d, "tsk_character_name.json"), encoding="utf-8") as f:
    m = json.load(f)

pat = re.compile(r'^speaker\s*=\s*"(.+)"')
unmapped = set()
for fp in glob.glob(os.path.join(d, "translations", "*.toml")):
    with open(fp, encoding="utf-8") as f:
        for line in f:
            g = pat.match(line)
            if g:
                n = g.group(1)
                if n not in m:
                    unmapped.add(n)

print(f"Unmapped speaker names ({len(unmapped)}):")
for x in sorted(unmapped):
    print(x)
