import pymysql
from get_connection import get_con


def add_customer():
    """inserts data into customer_details table."""
    print('registering a new customer')
    con = get_con()
    cursor = con.cursor()
    query = """
            INSERT INTO customer_details (full_name, phone_number, membership_type) 
            VALUES (%s,%s,%s)"""
    value = 1
    while value<= 3 :
        data = (input('full name: '), input('phone number: '), 
                    input('membership type: cardio/weights/crossfit/powerlifting: '))
        try:
            cursor.execute(query,data)
            break
        except Exception as e:
            print(f'error in the program: {e}')
            value += 1
    print('customer registered')
    con.commit()
    con.close()


def customer_signing():
    """Creating customer account."""
    print('creating customer signing in account')
    con = get_con()
    cursor = con.cursor()
    value = 1
    while value <=3 :
        try:
            id = cursor.execute(f"select customer_id from customer_details where phone_number = {input('enter your phone number: ')}")
            break
        except Exception as e:
            print(f'error: {e}')
            print('enter again')
            value += 1
    query = """
                INSERT INTO account_details (account_id, username,password,email)
                VALUES (%s,%s,%s,%s)"""
    value = 1
    while value <= 1 :
         print('enter data')
        data = (id,input('username: '), input('password: '), input('email: '))
        try:
            cursor.execute(query, data)
            break
        except Exception as e:
            print(f'error: {e}')
            value += 1
    print("customer's acoount created")
    con.commit()
    con.close()


  
