import requests
import json
import os

# link = "http://f-home.ecb2k16.com/jsin.php"
# with urllib.request.urlopen(link) as url:
#     data = json.loads(url.read().decode())
#     print(data)
#
#     for x in data["sensor"]:
#         print(x)
#         a = x["id"]
#         b = x["temp"]
#         c = x["humi"]
#         d = x["ppm"]
#         e = x["ldr"]
#         print(a, b, c, d, e)
#
#         for y in(a, b, c, d, e):
#             print (y, end=" || ")

import urllib.request, json
blt = []
url = "http://pokokeyakin.ecb2k16.com/jsin.php"
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode())
print(data)

nama = ""
for i in data["sensor"]:
    bt = i["humi"]
    nama = i['temp']
    try:
        os.mkdir(str(nama))
        print("Directory ", 'images/'+ str(nama), " Created ")

    except FileExistsError:
        print("Directory ", 'images/' + str(nama), " already exists")
    blt.append(bt)

# os.mkdir('abcd')
# print(blt)
# # print(bt)
# if bt == "0":
#     print("Kamera Aktif")
# else:
#     print("Kamera mati")