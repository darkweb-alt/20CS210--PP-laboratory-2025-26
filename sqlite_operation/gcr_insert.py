import sqlite3
conn_obj=sqlite3.connect('college.db')
cursor_obj=conn_obj.cursor()
query="INSERT INTO STUDENTS VALUES(101,'Pitambar','cse',95),(102,'Ram','ece',90),(103,'Shyam','Mtech',50)"
cursor_obj.execute(query)
conn_obj.commit()
conn_obj.close()