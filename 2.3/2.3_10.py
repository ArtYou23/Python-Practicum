x, y = 0, 0
a = input()
while a != "СТОП":
    if a == "СЕВЕР":
        i = int(input())
        y = y + i
    if a == "ВОСТОК":
        i = int(input())
        x = x + i
    if a == "ЮГ":
        i = int(input())
        y = y - i
    if a == "ЗАПАД":
        i = int(input())
        x = x - i
    a = input()
print(y)
print(x)