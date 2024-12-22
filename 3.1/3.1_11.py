n = int(input())
s = ''
for i in range(n):
    if i + 1 == n:
        s += input()
    else:
        s += input() + "\n"
m = s.split("\n")
w = input()
for i in m:
    if w.lower() in i.lower():
        print(i)