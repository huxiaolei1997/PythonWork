# -*- coding: utf-8 -*-
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = [generate_tr(name, score) for name, score in d.items()] # 注意：python3.x已经取消了iteritems()方法
print ('<table border="1">')
print ('<tr><th>Name</th><th>Score</th><tr>')
print ('\n'.join(tds))
print ('</table>')

# 运行结果：
# <table border="1">
# <tr><th>Name</th><th>Score</th><tr>
# <tr><td>Bart</td><td style="color:red">59</td></tr>
# <tr><td>Adam</td><td>95</td></tr>
# <tr><td>Lisa</td><td>85</td></tr>
# </table>