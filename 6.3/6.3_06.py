from requests import get


js = get("http://" + input() + "/users").json()
m = []
for i in js:
    m.append(i["last_name"] + " " + i["first_name"])
print("\n".join(sorted(m)))