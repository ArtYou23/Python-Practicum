from requests import get
from sys import stdin


adr = "http://" + input()
adr_n = [i.strip() for i in stdin]
sm = 0
for i in adr_n:
    sm += sum(get(adr + i).json())
print(sm)