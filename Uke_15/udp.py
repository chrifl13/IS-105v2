import socket
import sys

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, int :
    print 'Failed to create socket. Error Code : ' + str(int[0]) + ' Message ' + int[1]
    sys.exit()


# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , int:
    print 'Bind failed. Error Code : ' + str(int[0]) + ' Message ' + int[1]
    sys.exit()

print 'Socket bind complete'

#now keep talking with the client

while 1:
    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
    if data == "chin":
        data = "You put the chicken in."
        reply = data + ' What do you want to do next?'
    elif data == "chout":
        data = "You put the chicken out."
        reply = data + ' What do you want to do next?'
    elif data == "fxin":
        data = "You put the fox in."
        reply = data + ' What do you want to do next?' 
    
    elif data == "fxout":
        data = "You put the fox out."
        reply = data + ' What do you want to do next?'
    
    elif data == "grin":
        data = "You put the grain in."
        reply = data + ' What do you want to do next?'
    
    elif data == "grout":
        data = "You put the grain out."
        reply = data + ' What do you want to do next?'
    elif data == "row":
        data = "You went over the river."
        reply = data + ' What do you want to do next?'    
    

    s.sendto(reply , addr)
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()

s.close()