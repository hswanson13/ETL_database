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
            
            def find_id(table,column):
                columnFound = False
                while columnFound == False:
                    column_input = input(f'Input {column}: ')
                    if column_input == '': #if you do not need one don't input anything! rely on NOT NULL constraint!
                        return None
                    find_id_query = f'SELECT "id" FROM "{table}" WHERE {column}=%s'
                    cursor.execute(find_id_query,(column_input,))
                    id = cursor.fetchall()

                    if len(id) == 0:
                        print(f"{column_input} does not exist in database")
                        continue
                    else:
                        columnFound = True
                
                return id[0][0] #integer!

            #user sign in and get id
            accountFound = False
            while accountFound == False:
            #check username and password and make sure they are correct
                username = input('Input username: ')
                password = input('Input password: ') #should use getpass but for now it is fine

                validate_user_query = f'SELECT username, password FROM "user" WHERE username=%s AND password=%s'
                cursor.execute(validate_user_query, (username,password))
                account = cursor.fetchall() #if empty then they typed wrong password or username

                if len(account) == 0:
                    print("username or password incorrect")
                    continue
                else:
                    accountFound=True

 
            user_id = find_id('user','username')

            #maybe a better question is if this is an assembled module?
            mod_or_sensor = input('Are you testing a module (0) or a sensor (1)? ') #should make sure it is 0 or 1 here

            if mod_or_sensor == '0':
                module_id = find_id('module','module_serial_number')
                comp_id = None

            else:
                comp_id = find_id('component', 'component_serial_number')
                module_id = None

            test_type_id = find_id('test_lookup','test_name')

            data = input('Input the data: ')

            location = input('Where is this test occuring? ')

            add_data('test',get_column_names('test'),[user_id,module_id,comp_id,test_type_id,data,location])




            
            




            #add_data('assembly',get_column_names('assembly'),[module_id,stage_id,user_id,component_id,location,data])

except Error as e:
    print(e)