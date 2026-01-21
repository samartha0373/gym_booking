import create_database as cd
import create_tables as ct
import insert_data as id
print('creating database')
cd.create_database()
print('creating tables')
ct.create_tables()
print('adding customers')
id.add_customer()
print('creating customer account')
id.customer_signing()
