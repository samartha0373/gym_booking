import pymysql

def create_database():
    '''creates database for gym booking with mysql'''
    con = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password= 'password' )
    cursor = con.cursor()
    command = 'CREATE DATABASE IF NOT EXISTS gym_booking'
    cursor.execute(command)
    con.commit()
    print('database created!!!')
    con.close()


create_database()