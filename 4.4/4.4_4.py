def index(text):
    d = {}
    for i in text:
        if i.isalpha():
            if i not in d:
                d[i] = text.find(i)
    r = sorted(list((k, v) for k, v in d.items()), key=lambda x: x[0])
    for i in r:
        yield i