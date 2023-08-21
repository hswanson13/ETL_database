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

            the_table = 'module'
            
            #get all the column names
            columns = get_column_names(the_table,cursor)

            #make sure that inputted serial number doesn't already exist!
            module_serial_number = check_serial_number(the_table,'module_serial_number',cursor)
            location = input('What site is the module at/current location? ')

            add_data(the_table,columns,[location,module_serial_number],cursor) #MAKE SURE COLUMNS LIST AND INPUT LIST MATCH ONE TO ONE

except Error as e:
    print(e)