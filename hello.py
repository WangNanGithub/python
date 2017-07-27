# coding=utf-8

import requests
from bs4 import BeautifulSoup, NavigableString

'''
爬虫解析网页
'''

url = r'http://qq.ip138.com/idsearch/index.asp?action=idcard&userid=14240219921212061x'
response = requests.get(url=url)
response.encoding = 'GB2312'
# print 'status : ', response.status_code
# print 'content : ', response.text

soup = BeautifulSoup(response.text, 'html.parser')
# print soup
# print type(soup)

tables = soup.find_all('table')
# print type(tables)
# print type(tables[4].contents)


def parse_tag(t):
    if isinstance(t, NavigableString):
        if t.string.strip() != '':
            print 't : ', t
        return
    if len(t.contents) > 0:
        for i in t.contents:
            if not isinstance(i, NavigableString) and len(i.contents) > 0:
                parse_tag(i)
            elif isinstance(i, NavigableString) and i.string.strip() != '':
                print 'i2 : ', i.string

parse_tag(tables[4])




