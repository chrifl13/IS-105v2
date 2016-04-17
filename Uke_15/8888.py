'''
    udp socket client
    Silver Moon
'''
 
import socket   #for sockets
import sys  #for exit
 
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
 
host = 'localhost';
port = 8888;

while(1) :
    print "Write in the correct inputs, choose between chicken, fox and grain, then write if you want it in or out of the boat, like this 'chicken in'. If you want to row over write 'row'"
    msg = raw_input('')
    if msg == "row":
        msg = "row"
        try :
            #Set the whole string
            s.sendto(msg, (host, port))
             
            # receive data from client (data, addr)
            d = s.recvfrom(1024)
            reply = d[0]
            addr = d[1]
            
        except socket.error, msg:
            print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()
            
            
        print 'Server reply : ' + reply
        
    if msg == "chicken in":
        msg = "chin" 
        try :
            #Set the whole string
            s.sendto(msg, (host, port))
             
            # receive data from client (data, addr)
            d = s.recvfrom(1024)
            reply = d[0]
            addr = d[1]
            
        except socket.error, msg:
            print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()
            
            
        print 'Server reply : ' + reply
        
    elif msg == "chicken out":
            msg = "chout"
            try :
                #Set the whole string
                s.sendto(msg, (host, port))
                        
                # receive data from client (data, addr)
                d = s.recvfrom(1024)
                reply = d[0]
                addr = d[1]
                       
            except socket.error, msg:
                print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
                sys.exit()
                       
                       
                print 'Server reply : ' + reply
                
                
                
    elif msg == "fox in":
        msg = "fxin"
        try :
            #Set the whole string
            s.sendto(msg, (host, port))
             
            # receive data from client (data, addr)
            d = s.recvfrom(1024)
            reply = d[0]
            addr = d[1]
            
        except socket.error, msg:
            print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()
        
        print 'Server reply : ' + reply
        
    elif msg == "fox out":
        msg = "fxout"
        try :
            #Set the whole string
            s.sendto(msg, (host, port))
            
            # receive data from client (data, addr)
            d = s.recvfrom(1024)
            reply = d[0]
            addr = d[1]
            
        except socket.error, msg:
            print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()
            
            print 'Server reply : ' + reply
        
        
    elif msg == "grain in":
        msg = "grin"
        try :      
            #Set the whole string
            s.sendto(msg, (host, port))
                     
            # receive data from client (data, addr)
            d = s.recvfrom(1024)
            reply = d[0]
            addr = d[1]
                     
        except socket.error, msg:
            print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()
                 
            print 'Server reply : ' + reply        
        
        
    elif msg == "grain out":
        msg = "grout"
        try :
            #Set the whole string
            s.sendto(msg, (host, port))
             
            # receive data from client (data, addr)
            d = s.recvfrom(1024)
            reply = d[0]
            addr = d[1]
            
        except socket.error, msg:
            print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()
        
        print 'Server reply : ' + reply
    else:
        print "wrong"
        
        
       