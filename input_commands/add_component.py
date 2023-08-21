from getpass import getpass
import psycopg2
from psycopg2 import Error, connect

from common_functions import get_column_names, add_data, find_id, check_serial_number


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

            the_table = 'component'
            
            #get all the column names
            columns = get_column_names(the_table,cursor)

            #could add constraint that it checks to see if module_id is already "full" meaning it has all the components already in database!
            module_id = find_id('module','module_serial_number',cursor)
            
            component_type_id = find_id('component_type_lookup','component_name',cursor)
            location = input('What site is this component at/going to be at? ')
            component_serial_num = check_serial_number(the_table,'component_serial_number',cursor) #checks to make sure serial number doesn't already exist

            add_data(the_table,columns,[module_id,component_type_id,location,component_serial_num],cursor)


except Error as e:
    print(e)