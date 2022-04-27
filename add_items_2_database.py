import sqlite3 
import sys 

#THIS FILE ADDS AN ITEM TO THE TABLE IN THE DATABASE.

#ESTABLISH A DATABASE CONNECTION IN THE CURRENT WORKING DIRECTORY.
connection = sqlite3.connect("profile.db")

if True:
    print("Database connection established successfully...") 
else:
    print("Database connection failed")
    sys.exit(1)

#TO CREATE TABLE FOR PROFILE IN DATABASE WE NEED TO CREATE A CURSOR
cursor = connection.cursor()

#CREATE AN ITEM TO A TABLE IN DATABASE
cursor.execute("INSERT INTO profile VALUES ('Spider man', 'Parker', 'spider.parker@gmail.com')")


#ADD MANY ITEMS TO A DATABASE AT ONCE
# many_customers = [
#                 ('Wes', 'Brown', 'wes.brown@gmail.com'),
#                 ('Tanya', 'Blades', 'tanya@gmail.com'),
#                 ('sophia', 'reubens', 'sophia.reubens@babygirl.com')
#                ]
# cursor.executemany("INSERT INTO profile VALUES (?,?,?)", many_customers)

if True:
    print("Values inserted successfully...") 

#COMMIT OUR CONNECTION
connection.commit()

#CLOSE THE DATABASE CONNECTION 
connection.close()