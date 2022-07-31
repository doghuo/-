import re
import requests

r  = requests.get('https://github.com/favicon.ico')
#print(r.text)   str类型  
#print(r.content)图片是二进制类型
with open('favicon.ico','wb') as f:
    f.write(r.content)

                 #描述#   二进制数据
#下载github图标，print(r.text)是str类型会乱码，二进制类型写入favicon.ico