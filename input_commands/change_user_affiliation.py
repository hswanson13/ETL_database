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
            
            user_id = get_user(cursor) #returns id 
            #update password
            new_affiliation = input("Input new affiliation: ")

            #could add thing so it grabs the current and sets it to the opposite
            toggle_account_activation_query = 'UPDATE "user" SET affiliation=%s WHERE "id"=%s'
            cursor.execute(toggle_account_activation_query,(new_affiliation,user_id))

except Error as e:
    print(e)