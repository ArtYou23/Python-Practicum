a = int(input())
b = int(input())
c = int(input())
i = str(abs(a - b) / c)
if i[-2] == '.':
    i = i + '0'
print(i)