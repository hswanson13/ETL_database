from getpass import getpass
import psycopg2
from psycopg2 import Error, connect
from common_functions import get_user

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
            
            user_id = get_user(cursor)

            grab_curr_status_query = 'SELECT active_user FROM "user" WHERE "id"=%s'
            cursor.execute(grab_curr_status_query, (user_id,))
            curr_status = cursor.fetchall()[0][0]

            #could add thing so it grabs the current and sets it to the opposite
            toggle_account_activation_query = 'UPDATE "user" SET active_user=%s WHERE "id"=%s'
            cursor.execute(toggle_account_activation_query,(not curr_status,user_id)) #not curr_status flips activation

except Error as e:
    print(e)