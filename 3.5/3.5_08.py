f = []
with open(input(), encoding='UTF-8') as first:
    for line in first:
        f += line.split()
s = []
with open(input(), encoding='UTF-8') as second:
    for line in second:
        s += line.split()
t = sorted(set(s) ^ set(f))
with open(input(), "w", encoding='UTF-8') as answer:
    answer.write('\n'.join(t))