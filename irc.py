import sys
import socket
import string  
import math
import base64
import codecs

Cible = "Candy"
HOST="irc.root-me.org"
PORT=6667
NICK="Vala1"
IDENT="Valasulth"
REALNAME="Valasulth"
     
s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))

while 1:
    
    line = s.recv(2048)
    print ("Connection ok ....")
    s.send('JOIN #root-me_challenge\r\n')
    s.send('PRIVMSG ' + Cible + '!ep3')
    result = codecs.encode(line, "rot_13")
    s.send('PRIVMSG '+ Cible + ' :!ep3 -rep ' + result)
