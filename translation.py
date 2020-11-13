import os
import sys
import urllib.request
client_id = "s8yEGbbkj6hOb1C1ONje"
client_secret = "Ov11xvZnL0"
encText = urllib.parse.quote("무슨 게임 좋아해?")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    dic = response_body.decode('utf-8')
    dic = list(dic)
    trans = ''.join(dic[152:-37])
    print(trans)
    
else:
    print("Error Code:" + rescode)
