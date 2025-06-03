from requests import put
from json import dumps
from sys import stdin


adr = "http://" + input() + "/users/" + input()
put(adr, data=dumps({d[0]: d[1] for d in (i.strip().split("=") for i in stdin)}))