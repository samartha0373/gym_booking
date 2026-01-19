import get_connection

def test_conn():
    """checks whether get_connection returns connection to mysql."""
    con = get_connection.get_con()
    if con:
        print('successful!!!')
    else:
        print('unsuccessful')
