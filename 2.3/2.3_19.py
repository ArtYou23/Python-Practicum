a = 1
b = 1001
print((b - a) // 2 + a)
s = input()
for i in range(10):
    if s == "Угадал!":
        break
    elif s == "Меньше":
        b = (b - a) // 2 + a
        print((b - a) // 2 + a)
    elif s == "Больше":
        a = (b - a) // 2 + a
        print((a - b) // 2 + b)
    s = input()