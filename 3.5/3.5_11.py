import json

from numpy.ma.core import around


d = {}
m = []
with open(input(), encoding='UTF-8') as file:
    for line in file:
        m += line.split()
c = pos = mx = sm = middle = 0
mn = 10**10
for i in m:
    i = int(i)
    c += 1
    sm += i
    if i > 0:
        pos += 1
    if i < mn:
        mn = i
    if i > mx:
        mx = i
middle = sm / c
d["count"] = c
d["positive_count"] = pos
d["min"] = mn
d["max"] = mx
d["sum"] = sm
d["average"] = around(middle, decimals=2)
with open(input(), "w", encoding="UTF-8") as statistics:
    json.dump(d, statistics, ensure_ascii=False, indent=2)