import sqlite3 
import sys 

#THIS FILE CREATES A DATABASE CONNECTION IN THE CURRENT WORKING DIRECTORY.


#ESTABLISH A DATABASE CONNECTION IN THE CURRENT WORKING DIRECTORY.
connection = sqlite3.connect("profile.db")

if True:
    print("Database connection established successfully...") 
else:
    print("Database connection failed")
    sys.exit(1)

#TO CREATE TABLE FOR PROFILE IN DATABASE WE NEED TO CREATE A CURSOR
cursor = connection.cursor()

#CREATE A TABLE IN DATABASE
cursor.execute(""" CREATE TABLE profile (
    first_name text, 
    last_name text, 
    email text
)""")

#COMMIT OUR CONNECTION
connection.commit()

#CLOSE THE DATABASE CONNECTION 
connection.close()