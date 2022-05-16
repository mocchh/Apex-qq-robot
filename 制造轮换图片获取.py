import requests
import json


URL = "https://api.mozambiquehe.re/crafting?auth=979d0a73104cc447ebf3cd264030a319"
res = requests.get(URL)
jsonobj = json.loads(res.text)

assets = [asset[0]["itemType"]["asset"] for asset in jsonobj["bundleContent"]]
#plevel = jsonobj['current']['readableDate_end'] 
#prankscore = jsonobj['next']['map'] 
#prankname = jsonobj['next']['readableDate_start']

print(assets)