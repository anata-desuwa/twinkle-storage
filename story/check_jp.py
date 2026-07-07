import json, os, glob, re

d = os.path.dirname(__file__)
with open(os.path.join(d, "tsk_character_name.json"), encoding="utf-8") as f:
    m = json.load(f)

jp_keys = set(m.keys())
pat = re.compile(r'^speaker\s*=\s*"(.+)"')
still_jp = set()
for fp in glob.glob(os.path.join(d, "translations", "*.toml")):
    with open(fp, encoding="utf-8") as f:
        for line in f:
            g = pat.match(line)
            if g:
                n = g.group(1)
                if n in jp_keys:
                    still_jp.add(n)

print(f"Japanese names still in translations: {len(still_jp)}")
for x in sorted(still_jp):
    print(x)
