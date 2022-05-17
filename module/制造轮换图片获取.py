import requests
import json


URL = "https://api.mozambiquehe.re/crafting?auth=979d0a73104cc447ebf3cd264030a319"
res = requests.get(URL)
jsonobj = json.loads(res.text)

assets = [asset["itemType"]["asset"] for asset in jsonobj[0]["bundleContent"]]
assets2 = [asset["itemType"]["asset"] for asset in jsonobj[1]["bundleContent"]]
#image1 = pic1[0]['']
pic1 = assets[0]
pic2 = assets[1]
pic3 = assets2[0]
pic4 = assets[1]

