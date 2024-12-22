n, nn = [int(input()) for _ in range(2)]
s = ''
m = list([i for i in range(1, nn * n + 1)])
for i in range(len(m)):
    if i % nn == nn - 1:
        s += ' ' * (len(str(n * nn)) - len(str(m[i]))) + str(m[i]) + '\n'
    else:
        s += ' ' * (len(str(n * nn)) - len(str(m[i]))) + str(m[i]) + ' '
print(s)