import requests

url='https://www.douban.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}

get_response = requests.get(url,headers=headers,params=None)

post_response=requests.post(url,headers=headers,data=None,json=None)

print(post_response)

#print(get_response.text)

#print(get_response.content)

#print(get_response.json)

fo = open("post.txt", "w")
fo.write(str(post_response))
fo.close()

print("aa")

fo = open("text.txt", "w")
fo.write(str(get_response.json))
fo.close()
