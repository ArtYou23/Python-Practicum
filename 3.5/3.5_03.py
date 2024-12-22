from sys import stdin

for i in stdin:
    h = i.find("#")
    if h == 0:
        print(i[:h])