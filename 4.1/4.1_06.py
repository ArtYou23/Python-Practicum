def modern_print(ss):
    global s
    if ss not in s:
        s.add(ss)
        print(ss)


s = set()