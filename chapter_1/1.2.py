# 需要先安装beautifulsoup库
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://pythonscraping.com/pages/page1.html")
baseObj = BeautifulSoup(html.read())
print(baseObj.h1)