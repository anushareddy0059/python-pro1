import pymysql
conn=pymysql.connect(user='root',password='root',port=3306,database='pythonmysql')
cursor=conn.cursor()
try:
 query='''create table customer(id int primary key,name varchar(100),mobile bigint unique,balance bigint);'''
 cursor.execute(query)
except pymysql.err.OperationalError as e:
 print(f'{e}')
 def insert_record():
    query='''insert into customer(id,name,mobile,balance) values (1,'anu',9876145612,10000)'''
    cursor.execute(query)
    conn.commit()

def get_records():
  query='select*from customer'
  cursor.execute(query)
  records=cursor.fetchall()
  print(records)
def insert_dynamic(cid,name,mobile,balance):
  record=(cid,name,mobile,balance)
  query='insert into customer(id,name,mobile,balance) values(%s,%s,%s,%s)'
  cursor.execute(query,record)
  conn.commit()
  

