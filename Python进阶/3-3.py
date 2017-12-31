# -*- coding: utf-8 -*-

try:
    import json as json2
except ImportError:
    import simplejson as json2
print(json2.dumps({'python': 3.5}))