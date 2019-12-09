# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 19:28:55 2019

@author: dviswa1820
"""

import urllib.request
from bs4 import BeautifulSoup
response=urllib.request.urlopen("https://en.wikipedia.org/")
print(response.status)
headers=response.headers
content=response.read()
print(headers)
b=BeautifulSoup(content, 'html.parser')
#print(b.prettify())
print(b.get_text())
