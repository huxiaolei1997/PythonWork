# -*- coding: utf-8 -*-

# import requests
#
# res = requests.get("https://www.sina.com.cn/")
# res.encoding = "utf-8"
# print(res.text)

# from bs4 import BeautifulSoup
#
# html_sample = "<html><body><h1 id='title' class='title'>Hello,World</h1><h1 id='title2' class='title'>Hello,World2</h1><body></html>"
# soup = BeautifulSoup(html_sample, 'html.parser')
# h1select = soup.select('.title')
# print(h1select[0])
# print(h1select[0].text)
# for h1content in h1select:
#     print(h1content)
#     print(h1content['class'])
# print(h1select)

import requests
from bs4 import BeautifulSoup
res = requests.get("https://news.baidu.com/tech")
res.encoding = "utf-8"
# print(res.text)
soup = BeautifulSoup(res.text, "html.parser")
#print((soup.select(".l-middle-col"))[0].select(".ulist"))
# 爬取百度新闻中的互联网新闻
for techNews in soup.select(".column")[0].select(".ulist"):
    #print(len(techNews))
    for ulist in techNews.select("li"):
        #print(ulist.select("a"))
        print(ulist.select("a")[0].text + ", " + ulist.select("a")[0]['href'])
        #print(ulist.text +  ', ' + ulist['href'])
    #print(techNews)
    # for colNews in techNews
    #     print(colNews)
    #print(techNews)
# for ulist in (soup.select(".l-middle-col"))[0].select(".ulist"):
#     for aText in ulist.select("a"):
#         print(aText.text)

