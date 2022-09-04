import random
import re
import requests
import lxml
import time
import os
import socket


def ikunsystem():

    amount = input("請輸入你想要坤坤的數量\n a.少 b.中 c.大: ")
    if amount == "a":
        page = 30
        print('已選擇 少量30張')
    elif amount == "b":
        page = 60
        print('已選擇 中量60張')
    elif amount == "c":
        page = 90
        print('已選擇 大量90張')
    else:
        print("請輸入正確的選項！")
        time.sleep(3)
        return

    for index, pn in enumerate(range(0, int(page), 30)):
        socket.setdefaulttimeout(20)
        headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
        param = {'tn': 'resultjson_com',
                 'logid': '7809592584259704232',
                 'ipn': 'rj',
                 'ct': '201326592',
                 'is':'',
                 'fp': 'result',
                 'fr':'',
                 'word': "蔡徐坤打篮球表情包",
                 'queryWord': "蔡徐坤打篮球表情包",
                 'cl': '2',
                 'lm': '-1',
                 'ie': 'utf - 8',
                 'oe': 'utf - 8',
                 'adpicid':'',
                 'st':'',
                 'z':'',
                 'ic':'',
                 'hd':'',
                 'latest':'',
                 'copyright':'',
                 's':'',
                 'se':'',
                 'tab':'',
                 'width':'',
                 'height':'',
                 'face':'',
                 'istype':'',
                 'qc':'',
                 'nc': "1",
                 'expermode':'',
                 'nojc':'',
                 'isAsync':'',
                 'pn': pn,
                 'rn': "30",
                 'gsm': "1e",
                 '1662209018061':""}
        time.sleep(1)



        url = "https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDIsMSw2LDQsNSw3LDgsOQ%3D%3D&word=蔡徐坤打篮球表情包"
        response = requests.get(url=url, headers=headers, params=param)
        response.encoding = "utf-8"
        kun = response.text
        results = re.findall('"thumbURL":"(.*?)",', kun, re.S)

        for index2, result in enumerate(results):
            time.sleep(0.5)
            img = requests.get(result)
            if not os.path.exists("坤坤"):
                os.mkdir("坤坤")

            with open("坤坤\\" + str(index + 1) + "-" + str(index2 + 1) + ".jpg", "wb") as f:
                f.write(img.content)


if __name__ == '__main__':
    ikunsystem()
    print("成功獲取坤坤帥照！立即前往開團！")

#response = requests.get("https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDIsMSw2LDQsNSw3LDgsOQ%3D%3D&word=蔡徐坤打篮球表情包")#headers=headers)
#print(response.encoding)







