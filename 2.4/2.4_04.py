n = int(input())
c = 0
for i in range(n):
    k = input()
    c += sum(map(int, k))
print(c)