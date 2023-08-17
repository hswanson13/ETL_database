from getpass import getpass
#so you don't have passwords hardcoded into the python file!
import psycopg2

#conn.closed = 1 or 0, closed or open respectively
try:
    conn = psycopg2.connect(
        database = 'ETL_database',
        user='postgres',
        password=getpass("Enter password: "),
        host='localhost'
    )
    print(conn.closed)
    conn.close()
    print(conn.closed)
    print("Successfully Connected to ETL_database")
except:
    print("failed to connect")

