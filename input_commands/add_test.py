from getpass import getpass
import psycopg2
from psycopg2 import Error, connect

from common_functions import get_column_names, add_data, find_id, get_user

try:
    with connect(
        database = 'ETL_database',
        user='postgres',
        password=getpass("Enter password: "),
        host='localhost'
    ) as connection:
        
        with connection.cursor() as cursor:

            user_id = get_user(cursor)

            def is_unique(id1,id2,id1_input,id2_input,cursor):
                unique_step_query = f'SELECT "id" FROM test WHERE {id1}=%s AND {id2}=%s'
                cursor.execute(unique_step_query,(id1_input,id2_input))
                same_test = cursor.fetchall()
                if len(same_test) != 0:
                    raise Exception("This test step has already been performed, do blank if you wish to overwrite this step with this one")               

            #maybe a better question is if this is an assembled module?
            mod_or_sensor = input('Are you testing a module (0) or a sensor (1)? ') #should make sure it is 0 or 1 here

            if mod_or_sensor == '0':
                module_id = find_id('module','module_serial_number',cursor)
                comp_id = None
                test_type_id = find_id('test_lookup','test_name',cursor)
                is_unique('module_id','test_type_id',module_id,test_type_id,cursor)

            else:
                comp_id = find_id('component', 'component_serial_number',cursor)
                module_id = None
                test_type_id = find_id('test_lookup','test_name',cursor)
                is_unique('component_id','test_type_id',comp_id,test_type_id,cursor)


            #ensure not same test has been performed:
            #check the module_id, component_id and stage_id are not all the same: YOU CAN BUILD THIS INTO DATABASE TOO!


            data = input('Input the data: ')

            location = input('Where is this test occuring? ')

            add_data('test',get_column_names('test',cursor),[user_id,module_id,comp_id,test_type_id,data,location],cursor)

except Error as e:
    print(e)
