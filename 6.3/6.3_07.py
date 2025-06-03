from requests import get
from sys import stdin


try:
    js = get("http://" + input() + "/users/" + input()).json()
    text = "".join(i for i in stdin)
    for key in js:
        text = text.replace('{' + key + '}', str(js[key]))
    print(text)
except ValueError:
    print("Пользователь не найден")