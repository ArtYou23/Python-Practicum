n = int(input())
for i in range(n):
    u = input()
    if u.find("зайка") != -1:
        print(u.find("зайка") + 1)
    else:
        print("Заек нет =(")