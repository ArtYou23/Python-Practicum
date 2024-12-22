F, N = input(), int(input())
data = []
with open(F, encoding='UTF-8') as f:
    for line in f:
        data.append(line)
for line in data[-N:]:
    print(line.strip())