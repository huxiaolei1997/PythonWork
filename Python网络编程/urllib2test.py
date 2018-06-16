# -*- coding: utf-8 -*
import urllib.request, http.cookiejar
url = "https://www.baidu.com"

print("第一种方法")
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print("第二种方法")
request = urllib.request.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

print("第三种方法")
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
response3 = opener.open(url)
print(response3.getcode())
print(cj)
print(response3.read())

print("第3.1种方法")
cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
response3 = opener.open(url)
print(response3.getcode())
print(cj)
print(response3.read())