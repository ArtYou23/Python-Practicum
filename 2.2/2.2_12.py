a = int(input())
b = int(input())
c = int(input())
aa = a < b + c
bb = b < a + c
cc = c < a + b
if aa and bb and cc:
    print("YES")
else:
    print("NO")