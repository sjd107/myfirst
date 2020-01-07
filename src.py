import requests
import json

url = "http://fanyi.baidu.com"

data = {
    "from":"zh",
    "to":"en",
    "query":"你好，世界"
}
headers1= {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

headers={"Referer":"https://fanyi.baidu.com/",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}


response = requests.post(url,data=data,headers=headers)
print(response)
print(response.content)

html = response.content.decode()
print(response.content.decode())
print(type(response.content.decode()))
dict=json.loads(html)
dict_ret = json.loads(html)
print(dict_ret)
#print(type(dict_ret))
#ret = dict_ret["trans"][0]["dst"]
#print(ret)