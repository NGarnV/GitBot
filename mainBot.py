import socket
import string
import time

server = "efnet.port80.se"
channel = "#123"
botnick = "Kjell"
password = ""


def ping():
    i.send("Pong: ping\n")

def sendmsg(recipient, msg):  # This is the send message function, it simply sends messages to the channel.
    i.send("PRIVMSG " + recipient + " :" + msg + "\n")


def joinchan(chan):  # This function is used to join channels.
    i.send("JOIN " + chan + "\n")

i = socket.socket()
i.connect((server, 6667)) # kobler til serveren som vi allerede har definert.
i.send("USER " + botnick + " " + botnick + " " + botnick + " Noe dritt \n")
i.send("NICK " + botnick + "\n")
joinchan(channel)




while 1:
    ircmsg = i.recv(1024)

    print (ircmsg)

    if "PING :" in ircmsg:
        ping()
        

    elif ":Test" in ircmsg and channel in ircmsg:
        sendmsg(channel + "Test")



        
       

    
        


