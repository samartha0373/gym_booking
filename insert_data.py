import pymysql
from get_connection import get_con



def insert_data():
    con = get_con()
    cursor = con.cursor()
    query = """
            INSERT INTO customer_details (first_name, last_name, address, email) 
            VALUES (%s,%s,%s,%s)"""
    data = ('sameer','karki','woolwich','sameer@gmail.com')
    cursor.execute(query,data)
    con.commit()
    con.close()


insert_data()
    
  