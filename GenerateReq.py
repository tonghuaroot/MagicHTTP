# 将HTTP报文转为python脚本的脚本
import requests

Host = ''
User_Agent = ''
Accept = ''
Accept_Language = ''
Accept_Encoding = ''
Referer = ''
X_Requested_With = ''
Content_Type = ''
Content_Length = ''
Cookie = ''
Connection = ''
Content_Type = ''
Content_Length = ''


f = open('get_test.txt','r',encoding='utf-8')
data = f.readlines()
method = data[0].split(' ')[0]
uri = data[0].split(' ')[1]
data.pop(0)
data.pop()
for i in data:
    http_head_field = i.split(': ')[0]
    http_head_value = i.split(': ')[1].strip('\n')
    if http_head_field == 'Host':
        Host = http_head_value
        url = http_head_value+uri
    elif http_head_field == 'User-Agent':
        User_Agent = http_head_value
    elif http_head_field == 'Accept':
        Accept = http_head_value
    elif http_head_field == 'Accept_Language':
        Accept_Language = http_head_value
    elif http_head_field == 'Accept_Encoding':
        Accept_Encoding = http_head_value
    elif http_head_field == 'X_Requested_With':
        X_Requested_With = http_head_value
    elif http_head_field == 'Referer':
        Referer = http_head_value
    elif http_head_field == 'Cookie':
        Cookie = http_head_value
    elif http_head_field == 'Connection':
        Connection = http_head_value
    elif http_head_field == 'Content_Type':
        Content_Type = http_head_value
    elif http_head_field == 'Content-Length':
        Content_Length = http_head_value

headers = {
'Host':Host,
'User-Agent':User_Agent,
'Accept':Accept,
'Accept-Language':Accept_Language,
'Accept-Encoding':Accept_Encoding,
'Referer':Referer,
'X-Requested-With':X_Requested_With,
'Content-Type':Content_Type,
'Content-Length':'Content_Length',
'Cookie':Cookie,
'Connection':Connection
}

url = 'http://'+url
if method == "GET":
    r = requests.get(url, headers=headers)
elif method == "POST":
    r = requests.post(url, headers=headers, data=payload)


print("请求URL："+url)
print("请求方法："+method)
#print(r.text)

f.close()