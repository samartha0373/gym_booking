import pymysql

def get_con():
    '''returns the connection to mysql.'''
    try:
        con = pymysql.connect(
            host = '127.0.0.1',
            user = 'root',
            password = 'password')
        print('connection created')
        return con
    except Exception as e:
        print(f'error in mysql connection {e}.')
        return None


def con_test():
    con = get_con()
    if con:
        print('connection established successfully.')
    else:
        print('failed')


def create_database():
    '''creates database for gym booking with mysql'''
    con = get_con()
    cursor = con.cursor()
    command = 'CREATE DATABASE IF NOT EXISTS booking1'
    cursor.execute(command)
    con.commit()
    print('database created!!!')
    con.close()


def create_tables():
    '''creates tables for gym booking with mysql'''
    con = get_con()
    cursor = con.cursor()
    customer_details = """
                CREATE TABLE IF NOT EXISTS booking.customer_details (
                customer_id INT PRIMARY KEY AUTO_INCREMENT,
                first_name VARCHAR(30) NOT NULL,
                midle_name VARCHAR(30),
                last_name VARCHAR(30) NOT NULL,
                address VARCHAR(50) NOT NULL,
                email VARCHAR(50) UNIQUE) """
    account_details = """
                CREATE TABLE IF NOT EXISTS booking.account_details(
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
    create_database()
    print('database created successfully')
    # print('creating tables')
    # create_tables()
    # print('tables created successfully')


main()