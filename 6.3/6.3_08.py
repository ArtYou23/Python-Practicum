from requests import post
from json import dumps


adr = "http://" + input() + "/users"
post(adr, data=dumps({"username": input(), "last_name": input(), "first_name": input(), "email": input()}))