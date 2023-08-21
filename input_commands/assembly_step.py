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
            
            #needs new feature so you cant do pick and place or otherones more than once? 
            #maybe you would but it should actually just update the current value... need that to be a feature if it is the same do an update

            #you also shouldnt be able to pick and place the same component on multiple modules
            user_id = get_user(cursor)
            module_id = find_id('module','module_serial_number',cursor) #actually based off this it should get teh component_id's to choose from
            stage_id = find_id('assembly_lookup','stage_name',cursor)

            location = input('Where has asssembly stage taken place? ')
            data = input('Input assembly data: ')

            component_id = find_id('component','component_serial_number',cursor)

            #kind of sloppy way to do this, printed out the return of get column names and lines it up in the list here...
            add_data('assembly',get_column_names('assembly',cursor),[module_id,stage_id,user_id,component_id,location,data],cursor)

except Error as e:
    print(e)