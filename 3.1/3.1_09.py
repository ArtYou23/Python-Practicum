a = input()
while a != '':
    if a.find("#") == 0:
        a = a
    elif a.find("#") == -1:
        print(a)
    else:
        print(a[:(a.find("#"))])
    a = input()