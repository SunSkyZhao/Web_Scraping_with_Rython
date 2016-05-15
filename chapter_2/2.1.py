from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

class Spider:
    def __init__(self):
        self.start_url = "http://pythonscraping.com/pages/warandpeace.html"

    def get_html(self,url):
        html = urlopen(self.start_url)
        return html

    def get_element(self,html):
        bsObj = BeautifulSoup(html.read())
        return bsObj

    def do_something(self,code):
        # 查找所有的属性为绿色的人名
        nameList = code.findAll("span", {"class":"green"})
        for name in nameList:
            print(name.get_text())
        # 查找内容包含某字符的标签数量
        num = code.findAll(text="XXX")
        print(len(num))
        # 查找特定属性的标签
        allText = code.findAll(id="123")
        allText = code.findAll("",{"id":"222"})
        allText = code.findAll("",{"class":"green"})
        print(allText[0].get_text())

spider = Spider()
# url = "http://pythonscraping.com/pages/warandpeace.html"
html = spider.get_html(spider.start_url)
code = spider.get_element(html)
spider.do_something(code)