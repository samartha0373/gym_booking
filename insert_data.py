import pymysql
from get_connection import get_con



def insert_customer_details():
    """inserts data into customer_details table."""
    con = get_con()
    cursor = con.cursor()
    query = """
            INSERT INTO customer_details (first_name, last_name, address, email) 
            VALUES (%s,%s,%s,%s)"""
    data = ('sameer','karki','woolwich','sameer@gmail.com')
    cursor.execute(query,data)
    con.commit()
    con.close()


insert_customer_details()
    
  