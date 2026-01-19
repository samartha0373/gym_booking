import pymysql
from get_connection import get_con


def create_tables():
    '''creates tables customer_details and account_details for gym booking with mysql'''
    con = get_con()
    cursor = con.cursor()
    customer_details = """
                CREATE TABLE IF NOT EXISTS customer_details (
                customer_id INT PRIMARY KEY AUTO_INCREMENT,
                first_name VARCHAR(30) NOT NULL,
                midle_name VARCHAR(30),
                last_name VARCHAR(30) NOT NULL,
                address VARCHAR(50) NOT NULL,
                email VARCHAR(50) UNIQUE) """
    account_details = """
                CREATE TABLE IF NOT EXISTS account_details(
                customer_id INT PRIMARY KEY,
                gender ENUM('male','female','others') NOT NULL,
                membership_type ENUM('cardio','crossfit','weights','powerlifting'),
                date_created DATE DEFAULT NULL,
                updated_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                            ON UPDATE CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES booking.customer_details(customer_id))"""
    cursor.execute(customer_details)
    cursor.execute(account_details)
    con.commit()
    con.close()


def main(): 
    create_tables()
    print('tables created successfully')


main()