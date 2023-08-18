from getpass import getpass
import psycopg2
from psycopg2 import Error, connect

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
                
                #remove autogenerated columns, just id and timestamps
                cols = [c for c in column_names if c[0] != 'id' if c[1] != 'timestamp without time zone']
                return cols
            
            def add_data(table,column_names, input_data):

                str_cols = ",".join([c[0] for c in column_names]) #list comprehension because it is a list of tuples (name,data_type)
                flags = ('%s,'*len(input_data))[:-1] #:-1 removes the last comma
                tup_input_data = tuple(input_data)

                add_data_query = f"""
                INSERT INTO "{table}" ({str_cols})
                VALUES ({flags})
                """
                cursor.execute(add_data_query,tup_input_data)
                return
            
            #get all the column names
            columns = get_column_names(the_table)
            
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
                        print(all_usernames)
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

            add_data(the_table,columns,input_data,)

except Error as e:
    print(e)