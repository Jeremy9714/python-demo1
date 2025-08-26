# 网络爬虫

# requests库
import requests

url = 'https://baidu.com/'
resp = requests.get(url)  # get请求
# print(resp.text)  # 响应内容
# print(resp.content.decode())


img_url = 'https://oss.ppter8.com/QbFxRGWBEo7PtWIAX89REWdEwD3vvFzsPIy6oTN7.webp'
img_resp = requests.get(img_url)
print(type(img_resp.content))

# with open('../files/pm.jpg', mode='wb') as target:
#     target.write(img_resp.content)

# with open('../files/baidu.html', mode='w', encoding='utf-8') as target:
#     target.write(resp.content.decode())


# print(resp.url)
# print(resp.encoding)
# print(resp.status_code)
# print(resp.headers)
# print(resp.request)
# print(resp.request.headers)
# print(resp.request.method)
# print(resp.cookies)

print('------------------------')

# User-Agent 即用户代理，简称“UA”，它是一个特殊字符串头。
# 网站服务器通过识别 “UA”来确定用户所使用的操作系统版本、CPU 类型、浏览器版本等信息。
# 而网站服务器则通过判断 UA 来给客户端发送不同的页面。
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
# print(response.request.headers)
# print(len(resp.content.decode()))
# print(len(response.content.decode()))


# User-Agent池 防止反爬
# UA_list = [
#     'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36'
# ]
#
# import random
#
# print(random.choice(UA_list))



# UA伪装
# from fake_useragent import UserAgent
#
# print(UserAgent().random)
