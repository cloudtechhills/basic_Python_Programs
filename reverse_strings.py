from time import sleep 
import logging

"""
 THIS PROGRAM RECEIVES A STRING AS AN INPUT, 
 THEN REVERSE THE STRING AND PRINTS THE OUTPUT.
 """

logging.basicConfig(filename="reverse.log", encoding='utf-8', level=logging.DEBUG,  format='%(asctime)s :: %(levelname)s :: %(message)s :: %(filename)s :: %(created)s')


print("Enter any string and I would Reverse it for you!")

strings = str(input(""))

if strings == '': 
    logging.error("String Input Missing")
    print("Program Missing String Input.")

else: 
    reverse_strings = strings[::-1]

    print()
    print("Before Reverse Function: " + strings)
    sleep(1)
    print()
    print("After Reverse Function: " + reverse_strings)
