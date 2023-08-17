from getpass import getpass
import psycopg2
from psycopg2 import Error, connect

import click


try:
    with connect(
        database = 'ETL_database',
        user='postgres',
        password=getpass("Enter password: "),
        host='localhost'
    ) as connection:
        
        with connection.cursor() as cursor:
            def get_column_names(table):
                #get all the column names
                column_names_query = f"""
                SELECT column_name, data_type
                FROM information_schema.columns
                WHERE table_name = '{table}'
                ;
                """
                cursor.execute(column_names_query)
                #cursor.execute(data_type_columns_query)
                column_names = cursor.fetchall()
                print(column_names)
                return column_names
            
            #get all the column names
            columns = get_column_names('user')
            
            row = []
            for col in columns:
                if col[0]=='id' or col[1]=='timestamp without time zone':
                    continue
                row.append(input(f"Input {col[0]} ({col[1]}): "))

            print(row)

except Error as e:
    print(e)