num, ev, od, eq = input(), input(), input(), input()
ff, ss, tt = "", "", ""
with open(num, encoding='UTF-8') as first:
    for line in first:
        m = []
        [m.append(i) for i in line.split()]
        ff += ' '.join([i for i in m if sum(int(k) % 2 == 0 for k in i) > sum(int(k) % 2 != 0 for k in i)]) + '\n'
        ss += ' '.join([i for i in m if sum(int(k) % 2 == 0 for k in i) < sum(int(k) % 2 != 0 for k in i)]) + '\n'
        tt += ' '.join([i for i in m if sum(int(k) % 2 == 0 for k in i) == sum(int(k) % 2 != 0 for k in i)]) + '\n'
with open(ev, "w", encoding='UTF-8') as ev:
    ev.write(ff[:-1])
with open(od, "w", encoding='UTF-8') as od:
    od.write(ss[:-1])
with open(eq, "w", encoding='UTF-8') as od:
    od.write(tt[:-1])