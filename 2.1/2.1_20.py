a = int(input())
b = int(input())
c = int(input())
d = int(input())
sm = a * b
for i in range(1, a):
    for j in range(1, a):
        if i * c + j * d == sm and i + j == a:
            print(i, j)