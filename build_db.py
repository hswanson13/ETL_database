from getpass import getpass
import psycopg2
from psycopg2 import Error, connect
try:
    with connect(
        database = 'ETL_database',
        user='postgres',
        password=getpass("Enter password: "),
        host='localhost'
    ) as connection:
        
        with connection.cursor() as cursor:

            db_relations = open("ETLdb.pgsql","r").read()
            #print(db_relations)
            cursor.execute(db_relations)
            connection.commit()

except Error as e:
    print(e)

