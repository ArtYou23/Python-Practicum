p = int(input())
v = int(input())
t = int(input())
if p > v and p > t:
    print("Петя")
if v > p and v > t:
    print("Вася")
if t > p and t > v:
    print("Толя")