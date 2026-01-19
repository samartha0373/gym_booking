import pymysql

def create_database():
    '''creates database for gym booking with mysql'''
    con = get_con()
    cursor = con.cursor()
    command = 'CREATE DATABASE IF NOT EXISTS booking'
    cursor.execute(command)
    con.commit()
    print('database created!!!')
    con.close()