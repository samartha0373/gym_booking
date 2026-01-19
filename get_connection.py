import pymysql

def get_con():
    '''returns the connection to mysql.'''
    try:
        con = pymysql.connect(
            host = '127.0.0.1',
            user = 'root',
            password = 'password',
            database= 'gym_booking')
        return con
    except Exception as e:
        print(f'error in mysql connection {e}.')
        return None
    
