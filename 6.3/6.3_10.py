from requests import delete


adr = "http://" + input() + "/users/" + input()
delete(adr)