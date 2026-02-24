import sqlite3
conn_obj=sqlite3.connect("college.db")
cursor_obj=conn_obj.cursor()
delete_query="Delete from students where id=103"
cursor_obj.execute(delete_query)
conn_obj.commit()
conn_obj.close()
