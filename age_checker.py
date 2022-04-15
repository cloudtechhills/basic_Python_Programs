import time
import sys
import logging 

current_year = 2022

logging.basicConfig(filename="age_checker.log", encoding='utf-8', level=logging.DEBUG,  format='%(asctime)s :: %(levelname)s :: %(message)s :: %(filename)s :: %(created)s')

Name = str(input("Enter your Name: "))
time.sleep(1)
Year = int(input("Enter your Birth Year: "))


def cal_age(Name, Year, current_year):
    if (Name == ''):
        time.sleep(1)
        print("Please enter your details above")
        logging.error("Name Entry Missing")
        sys.exit()

    else:
        age = current_year - Year
        time.sleep(1)
        print("{} is {} years old".format(Name, age))
        logging.info("Success. {} made use of this program.".format(Name))


if __name__ == "__main__": 
    cal_age(Name, Year, current_year)