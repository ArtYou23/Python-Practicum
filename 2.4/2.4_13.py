y = int(input())
x = int(input())
ll = len(str(x * y))
m = ''
for i in range(1, y + 1):
    for j in range(1, x + 1):
        ij = y * (j - 1) + i
        if ij > (x * y) - y:
            m += ' ' * (ll - len(str(ij))) + str(ij)
            m += '\n'
        if ij <= (x * y) - y:
            m += ' ' * (ll - len(str(ij))) + str(ij) + ' '
print(m)