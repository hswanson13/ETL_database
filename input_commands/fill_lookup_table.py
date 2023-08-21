from getpass import getpass
import psycopg2
from psycopg2 import Error, connect

from common_functions import get_column_names, add_data, find_id, get_user

#uses python code to kind of dynamically get information and names
#probably not the best way, for future commands it will all be hard coded :)
#thought is if the database schema changes you should check and change code anyways... also might move to an ORM anyways and in that case the extra work is irrelevant

try:
    with connect(
        database = 'ETL_database',
        user='postgres',
        password=getpass("Enter password: "),
        host='localhost'
    ) as connection:
        
        with connection.cursor() as cursor:
            
            lookup_table = input("Lookup Table: ")
            n_entries = int(input("Number of entries: "))

            inputs_lookup = [(input('entry name: '),) for n in range(n_entries)]

            lookup_col = get_column_names(lookup_table,cursor)[0][0] #since id is filtered out there is only one column! and the first string [0] in the tuple, column name

            lookup_add_names_query = f"""
            INSERT INTO "{lookup_table}"
            ({lookup_col})
            VALUES (%s)
            """

            cursor.executemany(lookup_add_names_query,inputs_lookup)

except Error as e:
    print(e)