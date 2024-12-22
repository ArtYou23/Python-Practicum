n = int(input())
mm = -10000000000000000000000000000
for i in range(n):
    m = []
    while (nn := input()) != "next":
        m.append(int(nn))
    mm = max(mm, (sum(m) / len(m)))
print(f"{mm:.2f}")