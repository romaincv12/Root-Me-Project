import sys
import socket
import string  
import math
import base64

Cible = "Candy"
HOST="irc.root-me.org"
PORT=6667
NICK="Vala"
IDENT="Vala"
REALNAME="Valasulth"
     
s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))


while 1:
    line = s.recv(2048)
    s.send('JOIN #root-me_challenge\r\n')
    s.send('PRIVMSG ' + Cible + ' :!ep3\r\n')

    rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

    result = string.translate(line, rot13)
    s.send('PRIVMSG '+ Cible + ' :!ep3 -rep ' + str(result) + '\r\n')