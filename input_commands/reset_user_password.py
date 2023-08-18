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

            #update password
            new_password = input("Input new password: ")

            #could add thing so it grabs the current and sets it to the opposite
            toggle_account_activation_query = 'UPDATE "user" SET password=%s WHERE username=%s'
            cursor.execute(toggle_account_activation_query,(new_password,username))

except Error as e:
    print(e)