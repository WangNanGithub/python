# coding=utf-8

import requests

'''
爬虫解析网页
'''

url = r'http://qq.ip138.com/idsearch/index.asp?action=idcard&userid=14240219921212061x'
response = requests.get(url = url)
print 'status : ', response.status_code
print 'content : ', response.text

