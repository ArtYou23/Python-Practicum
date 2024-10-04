y = int(input())
x = int(input())
ll = len(str(x * y))
m = ''
for i in range(1, x * y + 1):
    m += ' ' * (ll - len(str(i))) + str(i)
    if i % x != 0:
        m += ' '
    if i % x == 0:
        m += '\n'
print(m)