import mysql.connector
from db_config import db_config
data_to_insert=(10,"Television","25","80")
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()
insert_query="insert into e_waste_items  (id,name,credit,price) values (%s,%s,%s,%s)"
cursor.execute(insert_query,data_to_insert)
connection.commit()
cursor.close()
connection.close()