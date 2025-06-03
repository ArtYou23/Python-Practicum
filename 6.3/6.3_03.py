from requests import get


print(sum([i for i in get("http://" + input()).json() if isinstance(i, int)]))