tr = "А — A, Б — B, В — V, Г — G, Д — D, Е — E, Ё — E, Ж — Zh, З — Z, И — I, Й — I, К — K, Л — L, М — M, Н — N, О — O, "
tr += "П — P, Р — R, С — S, Т — T, У — U, Ф — F, Х — Kh, Ц — Tc, Ч — Ch, Ш — Sh, Щ — Shch, Ы — Y, Э — E, Ю — Iu, Я — Ia"
tt = tr.split(", ")
dict = {}
for i in tt:
    ttt = i.split(" — ")
    r = ttt[0]
    e = ttt[1]
    dict[r] = e
    dict[r.lower()] = e.lower()
dict["Ъ"] = ""
dict["Ь"] = ""
dict["ъ"] = ""
dict["ь"] = ""
print(dict)
n = input()
s = ""
for i in n:
    if i not in dict:
        s += i
    else:
        s += dict[i]
print(s)