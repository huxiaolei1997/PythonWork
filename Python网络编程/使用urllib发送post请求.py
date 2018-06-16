# -*- coding: utf-8 -*-
import urllib.request
from urllib import parse
from bs4 import BeautifulSoup

req = urllib.request.Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")

postData = parse.urlencode([
    ("StartStation", "e6e26e66-7dc1-458f-b2f3-71ce65fdc95f"),
    ("EndStation", "3301e395-46b8-47aa-aa37-139e15708779"),
    ("SearchDate", "2018/06/15"),
    ("SearchTime", "12:30"),
    ("SearchWay", "DepartureInMandarin")
])

req.add_header("Origin", "http://www.thsrc.com.tw")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
resp = urllib.request.urlopen(req, data=postData.encode("utf-8"))

#print(resp.read().decode("utf-8"))
result = BeautifulSoup(resp.read().decode("utf-8"), "html.parser")
#print(result.select(".menu_item"))
for menu in result.select(".menu_item"):
    print(menu.select("a")[0]['href'] + ", " + menu.select("a")[0].text)