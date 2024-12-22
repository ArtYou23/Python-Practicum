a = input().lower()
b, c = [int(input()) for _ in range(2)]
if "sum" in a:
    print(b + c)
elif "sub" in a:
    print(b - c)
elif "mult" in a:
    print(b * c)
elif "div" in a:
    print(b // c)