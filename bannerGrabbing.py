import socket 
import sys, os



def retBanner(IP, Port):
    """This Program Grabs the Banner of an Open Port in a Target Host

    Args:
        IP (_type_): _description_
        Port (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        

        socket.setdefaulttimeout(2)
        
        socket_connetion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        socket_connetion.connect((IP, Port))

        banner = socket_connetion.recv(1024)
        
        print(banner)
        
        
            
    except Exception as e:
        
        return e



        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"[+] Program Usage: Python3 {os.path.relpath(sys.argv[0])} IP_Address")
    
    if len(sys.argv) == 2:
        
        portList = [21,22,25,53,80,110,443]
        IP = sys.argv[1]
        for port in portList:
            retBanner(IP, port)
            

