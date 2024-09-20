a = int(input())
b = int(input())
c = int(input())
t = a * 60 + b + c
ch = t // 60
mn = t % 60
if ch >= 24:
    ch = ch % 24
if ch // 10 < 1:
    ch = '0' + str(ch)
if mn // 10 < 1:
    mn = '0' + str(mn)
print(ch, ':', mn, sep='')