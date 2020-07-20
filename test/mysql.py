import pymysql

#打开数据库连接
db = pymysql.connect("localhost","root","yuanyuan","yuanyuan")

cursor = db.cursor()
# sql = "insert into python_pet (name,color,age,sex) values (%s,%s,%s,%s)";
# cursor.execute(sql,("大黄","橘黄色","3","公"))
sql = "select * from python_pet"
cursor.execute(sql)

results =cursor.fetchall()
for row in results:
    print('我的宠物叫'+row[0]+",他的毛色是"+row[1]+",今年"+str(row[2])+"岁了，是一只小"+row[3]+"猫")
db.commit()

db.close()
