# Kode er hentet fra:
# http://www.binarytides.com/programming-udp-sockets-in-python


import socket
import sys
from PIL import Image
HOST = ''   # Interface
PORT = 8888 # Tilgjengelig port

# UDP socket samt forbereder evt feilmelding
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()


#  - sette opp forbindelsen
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

#samhandler med klienten
while 1:
    # motta data fra klient (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]

    if not data: 
        break
    if data == "Chicken" :

        reply = 'Gratulerer, du hadde riktig svar. current state: FG | MC state 1'
        s.sendto(reply , addr)
        print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
    
    elif not data: 
                break
    if data == "Fox" :
        
                    reply = 'Kylling koste seg meg kornposen. State : Kyllying > kornpose. Game over. Start over'
                    s.sendto(reply , addr)
                    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
                    
    elif not data: 
        break
    if data == "Grain" :
                            
        reply = 'Kylling alene med rev er ikke noe bra. Current state: Rev spiser kylling. Game over. Start over'
        s.sendto(reply , addr)
        print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
        
    elif not data: 
                break
    if data == "Chicken, Man, Grain, Chicken, Fox, Man, Chicken" :
                                    
                reply = 'Mannen kom seg over med alle tingene sine i behold'
                s.sendto(reply , addr)
                print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip() 
                
                img = Image.open('tilstandsdiagram.jpg')
                img.show()                 
                
    elif not data: 
        break
    if data == "Chicken, Man, Fox, Grain, Fox, Man, Chicken" :
        
        reply = 'Mannen kom seg over med alle tingene sine i behold'
        s.sendto(reply , addr)
        print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()                       
        
        img = Image.open('tilstandsdiagram.jpg')
        img.show()   
        
    elif not data: 
        break
    if data == "RowRight":
                
        reply = 'Mannen ror fra venstre til høyre'
        s.sendto(reply , addr)
        print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()                         
                
        
    elif not data: 
        break
    if data == "RowLeft":
                               
        reply = 'Mannen ror båten fra høyre til venstre siden av elva'
        s.sendto(reply , addr)
        print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()            
        
    else:

        reply = 'Ugyldig svar, Invalid state. proev igjen!'
        s.sendto(reply , addr)
        print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
        
        
        

s.close()

