from socket import *
from win32clipboard import *
import sys

OpenClipboard()
try:
    text=GetClipboardData(CF_TEXT)
except:
    print "Error in getting clipboard data!"
    sys.exit()
finally:
    CloseClipboard()

print "ClipShare Clipboard Sharing Version 1.0\nDeveloped by Akash Pallath and Arik Pamnani\nSending Module\n\n"
host = raw_input("Enter IP address of machine you want to connect to: ")
port = 6000

server_address = (host,port)
try:
    sock = socket()

    sock.connect((host,port))

    sock.sendto(text, server_address)
    s= sock.recv(1024)
    print "Message from server: %s" %(s)
    sock.close()
except:
    print "Could not connect to network"
    sys.exit()
