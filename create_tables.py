import pymysql
from get_connection import get_con


def create_tables():
    '''creates tables customer_details and account_details for gym booking with mysql'''
    con = get_con()
    cursor = con.cursor()
    customer_details = """
                CREATE TABLE IF NOT EXISTS customer_details (
                customer_id INT PRIMARY KEY AUTO_INCREMENT,
                full_name VARCHAR(40) NOT NULL,
                membership_type ENUM('cardio','crossfit','weights','powerlifting'),
                phone_number VARCHAR(15) NOT NULL UNIQUE,
                booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )"""
    account_details = """
                CREATE TABLE IF NOT EXISTS account_details(
                account_id INT PRIMARY KEY,
                username VARCHAR(20) UNIQUE NOT NULL,
                password VARCHAR(225),
                sign_in_out ENUM ('IN','OUT') DEFAULT 'OUT' ,
                in_out_time DATETIME DEFAULT CURRENT_TIMESTAMP,
                email VARCHAR(50) UNIQUE,
                FOREIGN KEY (account_id) REFERENCES customer_details(customer_id)
                )"""
    cursor.execute(customer_details)
    print('customer_details created')
    cursor.execute(account_details)
    print('account_details created')
    con.commit()
    con.close()
