from requests import get


js = get("http://" + input()).json()
print(js.get(input(), "No data"))