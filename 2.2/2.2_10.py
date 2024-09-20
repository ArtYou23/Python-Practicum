i = input()
a = int(i[1]) + int(i[2])
b = int(i[0]) + int(i[1])
if a > b:
    print(a, b, sep='')
else:
    print(b, a, sep='')