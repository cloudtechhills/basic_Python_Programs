import qrcode  
import os 


###THIS PROGRAM CONVERTS A STRING OF TEXT TO A QRCODE IMAGE.

title="""
 _____         _     _   _ _____         _
|_   _|__  ___| |__ | \ | |___ / _ __ __| |
  | |/ _ \/ __| '_ \|  \| | |_ \| '__/ _` |
  | |  __/ (__| | | | |\  |___) | | | (_| |
  |_|\___|\___|_| |_|_| \_|____/|_|  \__,_|
"""

print(title)

text = str(input("Enter Text to convert to QR Code Format: "))

output_format = str(input("\nEnter File Name for the Generated QRcode Image: : "))


qrcode_format = qrcode.make(text)

qrcode_image = qrcode_format.save(output_format + ".jpg")

if True: 
    print("\n" + output_format + ".jpg" + " Saved Successfully")