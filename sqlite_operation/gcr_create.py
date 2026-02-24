import sqlite3
conn_obj=sqlite3.connect("college.db")
cursor_obj=conn_obj.cursor()
querycreate="CREATE TABLE STUDENTS(ID int Primary Key, name text, department text,marks int)"
cursor_obj.execute(querycreate)

conn_obj.commit()
conn_obj.close()




