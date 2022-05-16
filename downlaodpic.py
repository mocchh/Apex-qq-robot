import requests
import json


URL = f"https://api.mozambiquehe.re/maprotation?auth=979d0a73104cc447ebf3cd264030a319"
res = requests.get(URL)
jsonobj = json.loads(res.text)
pname = jsonobj['bundle']['map'] 
plevel = jsonobj['current']['readableDate_end'] 
prankscore = jsonobj['next']['map'] 
prankname = jsonobj['next']['readableDate_start']





url1 = "https://legion.apexlegendsstatus.com//cache//e50d6e0f6373649f15e95deb6e157816.png"

r = requests.get(url1)

image = r.content

with open(url1.split('/')[-1],'wb') as f:
    f.write(image)


url2 = "https://legion.apexlegendsstatus.com//cache//efd911e9eed31e66c274ef51c8c895b7.png"

r = requests.get(url2)

image = r.content

with open(url2.split('/')[-1],'wb') as f:
    f.write(image)


url3 = "https://legion.apexlegendsstatus.com//cache//efd911e9eed31e66c274ef51c8c895b7.png"

r = requests.get(url3)

image = r.content

with open(url3.split('/')[-1],'wb') as f:
    f.write(image)


url4 = "https://legion.apexlegendsstatus.com//cache//efd911e9eed31e66c274ef51c8c895b7.png"

r = requests.get(url4)

image = r.content

with open(url4.split('/')[-1],'wb') as f:
    f.write(image)