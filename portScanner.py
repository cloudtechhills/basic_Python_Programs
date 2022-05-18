import socket 
from time import sleep
import sys
import pyfiglet

from datetime import datetime
  


def intro(ip):
    ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
    print(ascii_banner)

    # Add Banner
    print("-" * 50)
    print("Scanning Target: " + ip)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)

def portScanner(ip):
    
    """
    SUMMARY:
    
    Args:
        ip (_type_): IP ADDRESS
    """
    try:
        intro(ip)
        for port in range(1, 65535):
            socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
            socket.setdefaulttimeout(1)
            result = socket_connection.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is Open.")
            socket_connection.close()
    except KeyboardInterrupt:
            print("[+] Program Shutting Down due to KeyBoardInterrupt Error!")
            sys.exit(1)
    except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            sys.exit(1)
    except socket.error:
            print("\ Server not responding !!!!")
            sys.exit(1)




def commandLine_Arg():
    if len(sys.argv) != 2 :
        print(f"[+] Format: {sys.argv[0]} <Target IP To Scan>")
        sys.exit(1)
    else:
        print("Welcome to my PortScanner")
        sleep(1)
        ip = sys.argv[1]
        portScanner(ip)
        
   




commandLine_Arg()
