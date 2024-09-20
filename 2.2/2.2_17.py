a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif a == 0 and b != 0:
    print(f"{-c / b:.2f}")
elif d > 0 and a != 0:
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    if x1 < x2:
        print(f"{x1:.2f} {x2:.2f}")
    else:
        print(f"{x2:.2f} {x1:.2f}")
elif d == 0 and a != 0:
    print(f"{-b / (2 * a):.2f}")
else:
    print("No solution")