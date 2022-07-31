import requests 
import re
from requests.auth import HTTPBasicAuth

r = requests.get('https://ssr1.scrape.center/')
#print(r.text)   数据源代码
#<h2 data-v-7f856186="" class="m-b-sm">aaa Concubine</h2>
pattern = re.compile('<h2.*?>(.*?)</h2>',re.S)
titles = re.findall(pattern,r.text)
print(titles)