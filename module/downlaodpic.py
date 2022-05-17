import requests
import json
import PIL.Image as Image
import os


URL = "https://api.mozambiquehe.re/crafting?auth=979d0a73104cc447ebf3cd264030a319"
res = requests.get(URL)
jsonobj = json.loads(res.text)

assets = [asset["itemType"]["asset"] for asset in jsonobj[0]["bundleContent"]]
assets2 = [asset["itemType"]["asset"] for asset in jsonobj[1]["bundleContent"]]
pic1 = assets[0]
pic2 = assets[1]
pic3 = assets2[0]
pic4 = assets2[1]
#获取URL


url1 = pic1

r = requests.get(url1)

image = r.content

with open(url1.split('/')[-1],'wb') as f:
    f.write(image)


url2 = pic2

r = requests.get(url2)

image = r.content

with open(url2.split('/')[-1],'wb') as f:
    f.write(image)


url3 = pic3

r = requests.get(url3)

image = r.content

with open(url3.split('/')[-1],'wb') as f:
    f.write(image)


url4 = pic4

r = requests.get(url4)

image = r.content

with open(url4.split('/')[-1],'wb') as f:
    f.write(image)
#下载图片
