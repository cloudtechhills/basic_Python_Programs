import sqlite3 

#THIS FILE UPDATES A DATABASE.


#ESTABLISH A DATABASE CONNECTION IN THE CURRENT WORKING DIRECTORY.
connection = sqlite3.connect("profile.db")

if True:
    print("Database connection established successfully...") 


#TO CREATE TABLE FOR PROFILE IN DATABASE WE NEED TO CREATE A CURSOR
cursor = connection.cursor()

#UPDATE THE DATABASE 
cursor.execute(""" UPDATE profile SET first_name = 'Tanya'
                WHERE rowid = 5 
            """)

#COMMIT OUR CONNECTION
connection.commit()


#HERE WE WILL QUERY THE DATABASE.
cursor.execute("SELECT rowid, * FROM profile")

#PUT THE ITEMS FROM THE DATABASE IN A VARIABLE 
items = cursor.fetchall()

print("[X] Updating The Database...")
print("=========="*7)

#LOOP THROUGH THROUGH ITEMS
for item in items:
    print(item)
   

