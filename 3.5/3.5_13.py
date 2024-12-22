import json
from sys import stdin


file = input()
with open(file, encoding="UTF-8") as f:
    data = json.load(f)
for line in stdin:
    before = line[:line.find('=')].rstrip()
    after = line[line.find('==') + 2:].lstrip().rstrip()
    data[before] = after
with open(file, "w", encoding="UTF-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)