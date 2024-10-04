n = int(input())
pr = int(input())
m = ''
c = cc = 0
for i in range(1, n + 1):
    ccc = 1
    for j in range(1, n + 1):
        ccc += 1
        if ccc % (n + 1) != 0:
            if ((pr - len(str(i * j))) / 2) == ((pr - len(str(i * j))) // 2):
                m += " " * ((pr - len(str(i * j))) // 2) + str(i * j) + " " * ((pr - len(str(i * j))) // 2) + "|"
            if ((pr - len(str(i * j))) / 2) != ((pr - len(str(i * j))) // 2):
                m += " " * ((pr - len(str(i * j))) // 2) + str(i * j)
                m += " " * (pr - len(str(i * j)) - ((pr - len(str(i * j))) // 2)) + "|"
        if ccc % (n + 1) == 0:
            if ((pr - len(str(i * j))) / 2) == ((pr - len(str(i * j))) // 2):
                m += " " * ((pr - len(str(i * j))) // 2) + str(i * j) + " " * ((pr - len(str(i * j))) // 2) + "\n"
                if i != j or i != n:
                    m += "-" * (pr * n + n - 1) + "\n"
            if ((pr - len(str(i * j))) / 2) != ((pr - len(str(i * j))) // 2):
                m += " " * ((pr - len(str(i * j))) // 2) + str(i * j)
                m += " " * (pr - len(str(i * j)) - ((pr - len(str(i * j))) // 2)) + "\n"
                if i != j or i != n:
                    m += "-" * (pr * n + n - 1) + "\n"
print(m)