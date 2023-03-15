#Code to handle all mysql queries using a single python function
#for ubuntu refer "https://stackoverflow.com/questions/39281594/error-1698-28000-access-denied-for-user-rootlocalhost" for installataion

import mysql.connector as mc
from mysql.connector import Error

# MYSQL VARIABLES
HOST="localhost"
USER="rock"
PASS=""
DATABASE=""
TABLE=""

try:
  def connect():
    global mc
    db = mc.connect(host='localhost',
            database=DATABASE,
            user=USER,
            password=PASS,connection_timeout=180)
    return db  
    
  def status():
    db = connect() 
    mc=db.cursor(dictionary=True)
    if db.is_connected():  #Show DB status
      db_Info = db.get_server_info()
      print("Connected to MySQL Server version ", db_Info)
      mc.execute("select database();")
      record = mc.fetchone()
      print("You're connected to database: ", record)
          
  def create_table():   #Create table
    db = connect() 
    mc=db.cursor(dictionary=True)
    sql = f"create table {TABLE} (   \
            id varchar(6) primary key not null,  \
            name varchar(15),       \
            age int, \
            descr varchar(50), \
            adopted varchar(3), \
            ext varchar(5))"
    mc.execute(sql)
    db.commit()

  def table_insert(id,name,age,descr,adopted,ext):   #insert records
    db = connect()  
    mc=db.cursor(dictionary=True)
    sql = f"INSERT INTO {TABLE} (id,name,age,descr,adopted,ext) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (id,name,age,descr,adopted,ext)
    mc.execute(sql, val)
    db.commit()
    return({"status":"success"})
    
  def table_display():           #Display all records
    db = connect()  
    mc=db.cursor(dictionary=True)
    sql=f"select * from {TABLE} ORDER BY _id DESC "
    mc.execute(sql)
    ab = mc.fetchall()
    return ab
    
  def table_fetch(id): #fetch a records
    db = connect()  
    mc=db.cursor(dictionary=True)
    sql=f"select * from {TABLE} where id=%s"
    val = ([id])
    mc.execute(sql,val)
    for i in mc :
      #dict = {"_id":i[0],"id":i[1],"name":i[2],"age":i[3],"desc":i[4],"adopted":i[5],"ext":i[6]}
      #return (dict)
      return (i)    

  def table_update(id,parameter,value):      #Update Records
    db = connect()  
    mc=db.cursor(dictionary=True)
    sql = f"UPDATE {TABLE} SET {parameter} = %s WHERE id = %s"
    val = (value,id)
    mc.execute(sql,val)
    db.commit()
    return({"status":"success"})

  def table_updateall(id,name,age,descr,adopted,ext):      #Update Records
    db = connect()  
    mc=db.cursor(dictionary=True)
    sql = f"UPDATE {TABLE} SET name=%s,age=%s,descr=%s,adopted=%s,ext=%s WHERE id = %s"
    val = (name,age,descr,adopted,ext,id)
    mc.execute(sql,val)
    db.commit()
    return({"status":"success"})  

  def table_count():  #returns total number of records
    db = connect()  
    mc=db.cursor(dictionary=True)
    sql=f"SELECT COUNT(*) FROM {TABLE}"
    mc.execute(sql)
    for i in mc :
      return i["COUNT(*)"]
      

  def table_delete(id):
    db = connect()  
    mc=db.cursor(dictionary=True)
    sql = f"delete from {TABLE} where  id=%s"
    val = ([id])
    mc.execute(sql,val)
    db.commit()
    return({"status":"success"})
    
  def table_close():
    db = connect()  
    mc=db.cursor(dictionary=True)  
    mc.close()
    db.close()    

except Error as e:
  print("Error while connecting to MySQL", e)    

status()

'''
table_insert("iAlTLI", "cutu", 2, "mallu", "no", "jpeg")
table_update("dfsdf","age", 8)
i =  table_display()
print(i)
print(table_fetch("hgjg1"))
print(table_count())
table_delete("dfsdf")
'''
