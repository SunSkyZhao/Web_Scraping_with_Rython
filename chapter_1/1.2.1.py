# 需要先安装beautifulsoup库
from bs4 import BeautifulSoup
from urllib.request import urlopen

# 抛出异常
try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except html.HTTPErroe as e:
    print(e)
else:
    baseObj = BeautifulSoup(html.read())
    print(baseObj.h1)