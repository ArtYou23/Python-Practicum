from requests import get


adr = "http://" + input()
c = 0
while i := int(get(adr).text):
    c += i
print(c)