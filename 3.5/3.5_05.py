from sys import stdin

text = []
for line in stdin:
    line = line.strip("\n")
    [text.append(i) for i in line.split() if i.lower() == i.lower()[::-1]]
print('\n'.join(sorted(set(text))))