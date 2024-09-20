x = float(input())
y = float(input())
tr = ((y <= 5 / 3 * x + 35 / 3) and (x <= -4) and (y >= 0))
pr = ((0 <= y <= 5) and (-4 <= x <= 0))
kr = ((x ** 2 + y ** 2) <= 25) and (y >= 0)
du = ((x ** 2 + 2 * x - 35) <= 0) and (y <= 0)
os = (x ** 2 + y ** 2) <= 100
print(tr, pr, kr, du)
if tr or pr or kr or du:
    print("Опасность! Покиньте зону как можно скорее!")
elif os:
    print("Зона безопасна. Продолжайте работу.")
else:
    print("Вы вышли в море и рискуете быть съеденным акулой!")