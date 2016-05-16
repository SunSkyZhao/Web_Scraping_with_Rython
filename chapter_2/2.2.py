from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsOgj = BeautifulSoup(html.read())
# 找出子元素
for child in bsOgj.find("table",{"id":"giftList"}).children:
    print(child)

# 找出兄弟元素，不包括自己
for child in bsOgj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(child)

# 找出兄弟元素，只会返回一个
for child in bsOgj.find("table",{"id":"giftList"}).tr.previous_siblings:
    print(child)

# 获取父级元素
print(bsOgj.find("img",{"id":"img"}).parent.previous_siblings.get_text())