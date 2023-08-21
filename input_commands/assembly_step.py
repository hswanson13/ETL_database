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

            print("if the ETROC/LGAD are irrelevant to the assembly step, input nothing into the component_id, just hit return.")
            component_id = find_id('component','component_serial_number',cursor) #find_id checks if it even exists in the database to start
            
            #you can either supply a component or not, but will always need a module pcb
            if component_id is not None:
                
                module_id_match_query = 'SELECT module_id FROM component WHERE "id"=%s'
                cursor.execute(module_id_match_query,(component_id,))
                matched_module_id = cursor.fetchall()
                module_id = matched_module_id[0][0]
            else:
                module_id = find_id('module','module_serial_number',cursor)
            
            stage_id = find_id('assembly_lookup','stage_name',cursor)

            #check the module_id, component_id and stage_id are not all the same: YOU CAN BUILD THIS INTO DATABASE TOO!
            unique_assembly_step_query = 'SELECT "id" FROM assembly WHERE module_id=%s AND stage_id=%s AND component_id=%s'
            cursor.execute(unique_assembly_step_query,(module_id,stage_id,component_id))
            same_assembly = cursor.fetchall()
            if len(same_assembly) != 0:
                raise Exception("This assembly step has already been performed, do blank if you wish to overwrite this step with this one")



            location = input('Where has asssembly stage taken place? ')
            data = input('Input assembly data: ')

            #print(f'THis is user id and type: {user_id, type(user_id)}')
            #print(get_column_names('assembly',cursor))
            #kind of sloppy way to do this, printed out the return of get column names and lines it up in the list here...
            #does it change in time???? might if columns are redefined!!! so this is a dangerous way to add data!
            add_data('assembly',get_column_names('assembly',cursor),[user_id,module_id,stage_id,component_id,location,data],cursor)

except Error as e:
    print(e)