from sys import stdin

text = []
for line in stdin:
    text.append(line.strip("\n"))
search = text.pop(-1)
for i in text:
    if search.lower() in i.lower():
        print(i)