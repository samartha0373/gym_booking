import get_connection

con = get_connection.get_con()
if con:
    print('successful!!!')
else:
    print('unsuccessful')
    