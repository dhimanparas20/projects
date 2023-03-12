#Code to handle all mysql queries using a single python function
#for ubuntu refer "https://stackoverflow.com/questions/39281594/error-1698-28000-access-denied-for-user-rootlocalhost" for installataion

import mysql.connector as mc
from mysql.connector import Error
from os import system

system("clear")

# MYSQL VARIABLES
HOST="localhost"
USER="root"
PASS="Luffykiid@2069"
DATABASE="rockonrescue"
TABLE="rescue"

try:
  db = mc.connect(host='localhost',
                  database=DATABASE,
                  user=USER,
                  password=PASS)
  #mc=db.cursor()
  mc=db.cursor(dictionary=True)


  def status():
    if db.is_connected():  #Show DB status
      db_Info = db.get_server_info()
      print("------------------------------------------------------------------")
      print("Connected to MySQL Server version ", db_Info)
      mc.execute("select database();")
      record = mc.fetchone()
      print("You're connected to database: ", record)
      print("------------------------------------------------------------------")
    else:
      print("error")  

  def create_table():   #Create table
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
    sql = f"INSERT INTO {TABLE} (id,name,age,descr,adopted,ext) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (id,name,age,descr,adopted,ext)
    mc.execute(sql, val)
    db.commit()
    return({"status":"success"})

  def table_update(id,parameter,value):      #Update Records
    sql = f"UPDATE {TABLE} SET {parameter} = %s WHERE id = %s"
    val = (value,id)
    mc.execute(sql,val)
    db.commit()
    return({"status":"success"})

  def table_updateall(id,name,age,descr,adopted,ext):      #Update Records
    sql = f"UPDATE {TABLE} SET name=%s,age=%s,descr=%s,adopted=%s,ext=%s WHERE id = %s"
    val = (name,age,descr,adopted,ext,id)
    mc.execute(sql,val)
    db.commit()
    return({"status":"success"})  

  def table_display():           #Display all records
    sql=f"select * from {TABLE} "
    mc.execute(sql)
    ab = mc.fetchall()
    return ab

  def table_fetch(id): #fetch a records
    sql=f"select * from {TABLE} where id=%s"
    val = [id]
    mc.execute(sql,val)
    for i in mc :
      #dict = {"_id":i[0],"id":i[1],"name":i[2],"age":i[3],"desc":i[4],"adopted":i[5],"ext":i[6]}
      #return (dict)
      return (i)

  def table_count():  #returns total number of records
    sql=f"SELECT COUNT(*) FROM {TABLE}"
    mc.execute(sql)
    for i in mc :
      return i["COUNT(*)"]

  def table_delete(id):
    sql = f"delete from {TABLE} where  id=%s"
    val = ([id])
    mc.execute(sql,val)
    db.commit()
    return({"status":"success"})

except Error as e:
  print("Error while connecting to MySQL", e)    


#table_insert("hgjg1", "Ramu", 1, "lala lala", "yes", "jpg")
#table_update("dfsdf","age", 8)
#for i in table_disp():
#  print(i)
#print(table_fetch("hgjg1"))
#print(table_count())
#table_delete("dfsdf")
 
