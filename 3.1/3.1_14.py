k = input()
p = int(input())
kk = [int(i) ** p for i in k.split()]
print(*kk)