#!/usr/bin/python3

#TITLE: PYTHON EMAIL_SENDER
#CREATED BY: OZURUMBA CHINEDU FRANCIS
#DATE: 13/4/2022

###IMPORTANT NOTE:
#CREATE AN APP PASSWORD FROM YOUR GMAIL ACCOUNT AND LINK VIA CODE ENTRY HERE
#ENSURE YOU TURN OFF THE

#HERE, WE IMPORT THE NECESSARY MODULES 
from email import message
import smtplib
import logging 
from email.mime.text import MIMEText
from getpass import getpass 


print("Ensure You have the read the Note above.")
#INITIALIZE THE LOG FILE 
logging.basicConfig(filename='pythonMail.log',encoding='utf-8', level=logging.DEBUG,  format='%(asctime)s :: %(levelname)s :: %(message)s :: %(filename)s :: %(created)s')


#MY GOOGLE APP PASSWORD
sender_email = str(input("Enter sender's email address: ")) #SENDER'S EMAIL ADDRESS
password = getpass(prompt="Enter your Gmail account password: ") 
receiver_email = str(input("Enter receiver's email address: "))
subject = str(input("Enter Message Subject: ")) 
message_body = str(input("Enter your message"))

message = MIMEText(message_body)
message['Subject'] = subject
message['From'] = sender_email
message['To'] = receiver_email   




#INITIALIZE THE SERVER 
try:    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()       #START THE SERVER ON A SECURE TLS
        server.login(sender_email, password)  #LOGIN TO THE GMAIL SERVER
        if True:
            logging.info("Login Successful")
            print("Login successful")

        
        server.sendmail(sender_email, receiver_email, message.as_string())
        if True:
            logging.info("Mail was sent successfully")
            server.quit()
except  Exception as e:
    logging.error("Exception Error occured {}".format(e))

