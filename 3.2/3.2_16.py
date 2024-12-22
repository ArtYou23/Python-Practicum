s = set()
while (n := input().split()) != []:
    if len(n) > 1 and "зайка" in n:
        for i in range(len(n)):
            if n[i] == "зайка":
                if i == 0:
                    s.add(n[1])
                elif i == (len(n) - 1):
                    s.add(n[-2])
                else:
                    s.add(n[i - 1])
                    s.add(n[i + 1])
print("\n".join(sorted(s)))