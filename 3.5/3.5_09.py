f = []
with open(input(), encoding='UTF-8') as first:
    for line in first:
        if line:
            f.append(line.replace('\t', '').split())
with open(input(), "w", encoding='UTF-8') as second:
    for i in f:
        if i != []:
            second.write(' '.join(i) + '\n')