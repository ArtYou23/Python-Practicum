s = ''
a = "абвгдеёжзиклмнопрстуфхцчшщъыьэюя"
aa = "abcdefghijklmnopqrstuvwxyz"
p = input()
s += p
while p != "ФИНИШ":
    p = input()
    s += p
ss = s.lower().replace(" ", "")[:-5]
m = [0] * 33
c = 0
for i in a:
    m[c] = ss.count(i)
    c += 1
if sum(m) == 0:
    c = 0
    for i in aa:
        m[c] = ss.count(i)
        c += 1
    mm = max(m)
    cc = 0
    for i in m:
        if i == mm:
            print(aa[cc])
            exit()
        cc += 1
mm = max(m)
cc = 0
for i in m:
    if i == mm:
        print(a[cc])
        break
    cc += 1