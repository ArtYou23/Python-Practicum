a = str(input())
b = str(input())
if len(a) == 1:
    a = '00' + a
if len(a) == 2:
    a = '0' + a
if len(b) == 1:
    b = '00' + b
if len(b) == 2:
    b = '0' + b
r1 = (int(a[0]) + int(b[0])) % 10
r2 = (int(a[1]) + int(b[1])) % 10
r3 = (int(a[2]) + int(b[2])) % 10
print(r1, r2, r3, sep='')