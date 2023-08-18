# ETL_database
A database project to store testing and assembly information for the the construction of the Endcap Timing Layer detector in CMS

# ----SET UP THE DATABASE and INSTALL POSTGRESSQL-----
Install PostgresSQL:
more info here: https://ubuntu.com/server/docs/databases-postgresql
In a linux terminal do:
1. sudo apt install postgresql
2. sudo -i -u postgresql
3. createdb ETL_database

You check it is there by doing (in same terminal):
1. psql -d ETL_database
This should bring you into the database and using postgresql in the terminal where you can execture SQL commands

Now configure your password (you might have to exit the database, if it doesnt work refer to link above)

2. ALTER USER postgres with encrypted password 'your_password';

Now you can close this terminal.

# ---SET UP THE GITHUB REPOSITORY WITH SSH----
1. git clone git@github.com:user_name/ETL_database.git
2. cd ETL_database

Install packages for the repository so make sure you are in it:
I would also recommend you setting up your own virtual environment
it uses python=3.11.4

1. pip install psycopg2
2. python test_db_connection.py
If this says you successfully connected to the database you are good to go!
3. python build_db.py
This will build the database and all the data in it!


