import sqlite3
conn_obj=sqlite3.connect("college.db")
cursor_obj=conn_obj.cursor()
query1="SELECT * from STUDENTS"
cursor_obj.execute(query1)
cursor_obj.execute("SELECT * FROM STUDENTS WHERE MARKS>80")
for row in cursor_obj.fetchall():
    print(row)
conn_obj.commit()
conn_obj.close()