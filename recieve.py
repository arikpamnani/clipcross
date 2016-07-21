import socket

from socket import *
from win32clipboard import *
from win32con import *

print "ClipShare Clipboard Sharing Version 1.0\nDeveloped by Akash Pallath and Arik Pamnani\nReceiving Module\n\n"

host = ""                   #Accept connection from any machine.
port = 6000                 #We will communicate over port 6000 of this machine. Ports 0-1024 are restricted, ports 1025-65535 are not.

s=""

try:
    sock = socket()             #Create a network socket. By default, it is a TCP socket
    print "Socket successfully created"
    sock.bind((host,port))      #Binds to the port
    print "Socket successfully bound to port %d" %(port)

    sock.listen(1)              #We want to listen only to one connection at a time
    print "Socket listening for connections..."

    con, address = sock.accept()
    print "Recieved connection from %s" %(str(address))

    from Tkinter import *
    import tkMessageBox

    root = Tk()
    root.withdraw()

    query = tkMessageBox.askquestion('Incoming Clipboard Data', 'Do you wish to recieve clipboard data from %s?' %(str(address[0])), icon = 'warning')
    if query == 'yes':
        s= str(con.recv(65536))
        try:
            OpenClipboard()
            EmptyClipboard()
            SetClipboardData(CF_TEXT, s)
            CloseClipboard()
        except:
            print "Error in accessing clipboard data!!!"
            sys.exit()

        print "Recieved clipboard data from client"
        con.send("Thank you for connecting. Your data was successfully recieved.")
    else:
        con.send("The user you were trying to send data to declined your clipboard data.")

except:
    print "Error in networking!"
    sys.exit()
finally:
    con.close()


