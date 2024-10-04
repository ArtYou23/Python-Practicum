n = int(input())
print('А Б В')
for i in range(1, n):
    for j in range(1, n):
        for k in range(1, n):
            if i + j + k == n:
                print(i, j, k)