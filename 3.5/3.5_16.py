from sys import stdin


def norm(x):
    x = x.replace('\n', ' ')
    while '  ' in x:
        x = x.replace('  ', ' ')
    return x


string, flag = input(), 1
list = [x.strip() for x in stdin]
for name in list:
    with open(name, encoding="UTF-8") as f:
        data = ''.join(f.readlines()).lower()
        if string.lower() in norm(data):
            print(name)
            flag = 0
if flag == 1:
    print("404. Not Found")