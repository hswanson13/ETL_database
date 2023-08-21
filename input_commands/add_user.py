from getpass import getpass
import psycopg2
from psycopg2 import Error, connect

from common_functions import get_column_names, add_data


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
            the_table = 'user'
                  
            #get all the column names
            columns = get_column_names(the_table, cursor)
            
            input_data = []
            for col in columns:

                if col[0] == 'username':
                    #make sure that inputted username doesn't already exist!
                    unique = False
                    while unique == False:

                        test_input = input(f"Input {col[0]} ({col[1]}): ")

                        check_unique_user_query = """
                        SELECT username from "user";
                        """
                        cursor.execute(check_unique_user_query)
                        all_usernames = [i[0] for i in cursor.fetchall()]
                        if test_input not in all_usernames:
                            unique=True
                        else:
                            print("username already exists, try again")
                    
                    input_data.append(test_input)
                    continue
                
                elif col[0] == 'active_user':
                    input_data.append('1')
                    continue

                user_input = input(f"Input {col[0]} ({col[1]}): ")
                input_data.append(user_input)

            add_data(the_table,columns,input_data,cursor)

except Error as e:
    print(e)