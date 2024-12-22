from sys import stdin

text = stdin.read().strip("\n")
print(sum(int(i) for i in text.split() if i != ""))