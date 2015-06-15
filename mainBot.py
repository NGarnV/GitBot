import socket
import string
import time


server = "efnet.port80.se"
channel = "#123"
botnick = "Kjell"

def ping():
    ircsock.send("Pong: ping\n")

def sendmsg(recipient, msg):  # This is the send message function, it simply sends messages to the channel.
    ircsock.send("PRIVMSG " + recipient + " :" + msg + "\n")



def joinchan(chan):  # This function is used to join channels.
    ircsock.send("JOIN " + chan + "\n")

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # kobler til serveren som vi allerede har definert.
ircsock.send("USER " + botnick + " " + botnick + " " + botnick + " Noe dritt \n")
ircsock.send("NICK " + botnick + "\n")
joinchan(channel)


x=0

while 1:
    ircmsg = ircsock.recv(1024)

    print (ircmsg)

    if "PING :" in ircmsg:
        ping()

    if ":Test" in ircmsg and channel in ircmsg:
        tst = commands.Test(words)
        ircmsg(tst)
        while x<10:
            x+1
            print " /n"

    
        
  
            


