m = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
n = int(input())
c = 0
for i in range(n):
    print(m[c])
    c += 1
    if c == 5:
        c = 0