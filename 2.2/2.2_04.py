p = int(input())
v = int(input())
t = int(input())
if p > v and p > t:
    if v > t:
        print("1. Петя")
        print("2. Вася")
        print("3. Толя")
    else:
        print("1. Петя")
        print("2. Толя")
        print("3. Вася")
if v > p and v > t:
    if p > t:
        print("1. Вася")
        print("2. Петя")
        print("3. Толя")
    else:
        print("1. Вася")
        print("2. Толя")
        print("3. Петя")
if t > p and t > v:
    if p > v:
        print("1. Толя")
        print("2. Петя")
        print("3. Вася")
    else:
        print("1. Толя")
        print("2. Вася")
        print("3. Петя")