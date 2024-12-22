a = input()
c = 0
while a != '':
    if a[-3:] == "@@@":
        c = 0
        if a[:2] == "##":
            c = 0
    elif a[:2] == "##":
        print(a[2:])
    else:
        print(a)
    a = input()