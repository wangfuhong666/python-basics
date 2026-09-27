import pymysql

a = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': '仓库1',
    'charset': 'utf8'
}
aaa = pymysql.connect(**a)
bbb = aaa.cursor()
sql1 = 'select * from 表1'
bbb.execute(sql1)
# print(bbb.fetchall())
sql2 = 'insert into 表1 value(41396,"王福洪",86)'
try:
    bbb.execute(sql2)
    aaa.commit()
    print("插入成功")
except Exception as e:
    aaa.rollback()  # 出错时回滚事务
    print("插入失败：", e)  # 打印具体错误原因
    # 插入后立即查询，确认是否在当前连接的会话中存在
bbb.execute("select * from 表1 where id = 41396")  # 假设id是41396
print("插入后查询结果：", bbb.fetchall())  # 若能查到，说明数据在当前事务中存在，但未持久化