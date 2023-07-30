import mysql.connector as mcon

db=mcon.connect(host='localhost', user='root', passwd='1234')
cur=db.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS SCHOOL;")
cur.execute("USE SCHOOL;")
cur.execute("CREATE TABLE IF NOT EXISTS STUDENTS (ROLLNO INT, STNAME VARCHAR(20));")
db.commit()
cur.execute("INSERT INTO STUDENTS VALUES (1,'KARAN'),(2,'AAYAN');")
db.commit()
cur.execute("SELECT * FROM STUDENTS;")

for i in cur.fetchall():
    print(i)

db.close()
