#引入requests库
import requests
#requests
r = requests.head("http://www.hl345.xyz")
#r.status_code HTTP返回状态 判断url是否连接成功 200 成功
r.status_code
print(r.status_code)
#r.encoding根据HTTP headr 猜测网页编码方式
r.encoding = 'utf-8'
#r.apparent_encoding 根据HTTP 类容分析网页编码方式
r.apparent_encoding
#r.text HTTP响应类容的字符串形式
r.text
b= requests.packages

