# -*- coding: utf-8 -*-
import pymysql
# 注意这里的py文件不能命名为 pymysql，否则会提示出错
# 打开数据库连接
# db = pymysql.connect(host="127.0.0.1", port=3366, user="root", password="hxl2580", db="ysxy")
# #db = pymysql.connect("127.0.0.1", 3366, "root", "hxl2580", "ysxy")
# # 使用 cursor方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute() 方法执行 SQL查询
# cursor.execute("select * from user")
#
# # 使用 fetchone() 方法获取单条数据
# #data = cursor.fetchone()
# for row in cursor:
#     print(row)
# #print("Database version: %s" %data)
#
# # 关闭数据库连接
# db.close()
# cursor.close()

#db = pymysql.connect(host="139.196.140.168", port=3306, user="root", password="hxl2580", db="ysxy")
# 或这么写
# db = pymysql.connect(host="127.0.0.1", port=3366, user="root", password="hxl2580", db="ysxy")
#
# # 不能这么写
# # db = pymysql.connect("139.196.140.168", 3306, "root","hxl2580", "ysxy")
# #db = pymysql.connect("127.0.0.1", 3366, "root", "hxl2580", "ysxy")
# # 使用 cursor方法创建一个游标对象 cursor
# cursor = db.cursor()
# try:
#     # 使用 execute() 方法执行 SQL查询
#     cursor.execute("select * from user")
#
#     # 使用 fetchone() 方法获取单条数据
#     #data = cursor.fetchone()
#     # 获取所有结果
#     results = cursor.fetchall()
#     for row in results:
#         id = row[0]
#         user_name = row[1]
#         password = row[2]
#         note = row[3]
#         email = row[4]
#         account_owner = row[5]
#         print("id=%d, user_name=%s, password=%s, note=%s, email=%s, account_owner=%s"
#               %(id, user_name, password, note, email, account_owner))
#     #print("Database version: %s" %data)
#  # 捕获异常
# except:
#     print("Error: unable to fetch data")
# # 关闭游标
# cursor.close()
# # 关闭数据库连接
# db.close()

# 更新数据
db_update = pymysql.connect(host="127.0.0.1", port=3366, user="root", password="hxl2580", db="ysxy")
db_update_cursor = db_update.cursor()
# args = ('update_hello_5', 49)
# update_user_name = 'update_hello_3'
#sql = "update user set user_name = '%s' where id = 49" %(update_user_name); # 这样写会有 SQL注入 的风险，强烈建议 不要 这么写，建议参考下面的写法
try:
    # 执行 sql 语句
    #db_update_cursor.execute(sql)
    #
    update_user_name = "49;delete from user"
    id = 49
    #sql = "update user set user_name = 'dds' where id = %s" % (id)
    #db_update_cursor.execute(sql)
    #db_update_cursor.execute("update user set user_name = %s where id = 49", update_user_name)
    # 正确用法，可以有效的防止sql注入
    db_update_cursor.execute("update user set user_name = %s where id = %s", (update_user_name, id))
    print("执行")
    # 提交到数据库执行
    db_update.commit()
except Exception as e:
    # 发生错误时回滚
    db_update.rollback()
    print("发生错误：%s" %e)
# 关闭游标
db_update_cursor.close()
# 关闭数据库连接
db_update.close()