import requests
import json
from os import system
params = {"api":"1RUGoBHXqpk8zbdrCOIQ"}

res = requests.get(f"https://d506-106-78-78-172.ngrok.io/api",params=params)
#res = requests.get(f"https://d506-106-78-78-172.ngrok.io/api",json=params)
print(res)
print(res.text)
