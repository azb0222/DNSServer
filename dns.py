# DNS SERVER 

import socket 
 
port = 53 
ip = '127.0.0.1' #ip of loopback

#create a UDP socket using IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))

def buildresponse(data): 
    


#create an infinite to listen receive data
while 1: 
    data, addr = sock.recvfrom(512) 
    print(data)
    r = buildresponse(data)
    sock.sendto(r, addr) #send it back to the address we received request from 


