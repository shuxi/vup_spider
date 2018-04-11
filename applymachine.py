
#coding=utf-8

import requests
import re

p = '<a href=\"(\w+\.php\?ins_id=\w+)\" target="_blank">\w+</a> <font color=\"green\">'
pp = 'action=\"(\w+.php\?ins_id=\w+)\">'

url = r'http://115.156.135.252/dcms/userlogin.php'
para = {"username":'M201672704',"password":'123456'}

s = requests.session()

r = s.post(url,data=para)

html = r.text
result = re.search(p,html)
href =  'http://115.156.135.252/dcms/'+result.groups()[0]

r = s.get(href)

html = r.text
result = re.search(pp,html)
href =  'http://115.156.135.252/dcms/'+result.groups()[0]

s.post(href,data={'sel_num':12})

#print(r.text)