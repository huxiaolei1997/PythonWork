# -*- coding: utf-8 -*-
import urllib.request as request # 别名

req = request.Request("https://www.baidu.com")

req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")

resp = request.urlopen(req)

print(resp.read().decode("utf-8"))