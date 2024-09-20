p = int(input())
v = int(input())
t = int(input())
if p > v and p > t:
    if v > t:
        print("          Петя          ")
        print("  Вася")
        print("                  Толя")
        print("   II      I      III   ")
    else:
        print("          Петя")
        print("  Толя")
        print("                  Вася")
        print("   II      I      III   ")
if v > p and v > t:
    if p > t:
        print("          Вася")
        print("  Петя")
        print("                  Толя")
        print("   II      I      III   ")
    else:
        print("          Вася")
        print("  Толя")
        print("                  Петя")
        print("   II      I      III   ")
if t > p and t > v:
    if p > v:
        print("          Толя")
        print("  Петя")
        print("                  Вася")
        print("   II      I      III   ")
    else:
        print("          Толя")
        print("  Вася")
        print("                  Петя")
        print("   II      I      III   ")