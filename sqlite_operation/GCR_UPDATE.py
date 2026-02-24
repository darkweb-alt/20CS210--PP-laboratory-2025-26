# foR UPDATING 
import sqlite3
# conn_obj.sqlite3.connect("college.db")
conn_obj=sqlite3.connect("college.db")
cursor_obj=conn_obj.cursor()
update_query="update  students set marks=99 where id=103"
cursor_obj.execute(update_query)
conn_obj.commit()
conn_obj.close()
