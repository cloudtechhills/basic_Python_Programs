import pyshorteners as short
from time import sleep 

text="""
 _____         _     _   _ _____         _
|_   _|__  ___| |__ | \ | |___ / _ __ __| |
  | |/ _ \/ __| '_ \|  \| | |_ \| '__/ _` |
  | |  __/ (__| | | | |\  |___) | | | (_| |
  |_|\___|\___|_| |_|_| \_|____/|_|  \__,_|
"""

title = """
 _   _ ____  _         ____  _                _                       
| | | |  _ \| |       / ___|| |__   ___  _ __| |_ ___ _ __   ___ _ __ 
| | | | |_) | |       \___ \| '_ \ / _ \| '__| __/ _ \ '_ \ / _ \ '__|
| |_| |  _ <| |___     ___) | | | | (_) | |  | ||  __/ | | |  __/ |   
 \___/|_| \_\_____|___|____/|_| |_|\___/|_|   \__\___|_| |_|\___|_|   
                 |_____|                                              

"""
##THIS PROGRAM SHORTENS A LONG URL TO A SHORT SIZED URL FOR ANY PURPOSE.


print(text)
sleep(1)
print(title)
link = str(input("Enter the URL link: "))

shortener = short.Shortener()

tiny_url = shortener.tinyurl.short(link)

print("\nThis is the Shortened URL: {}".format(tiny_url))

print("\n===========Thank You for Using This Program=============")
print("\n[X] Help me to update this program if you feel there is a better way to execute this idea.")