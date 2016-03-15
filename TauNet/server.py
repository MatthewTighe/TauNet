#This is the server program for the TauNet system.
#Copyright (c) 2015 Matthew Tighe

host = ''
port = 6283

import socket, cipher
key = input("Please enter your TauNet key: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
while(1):
    s.listen(5)
    conn, addr = s.accept()
    msg = conn.recv(1024)
    if(msg == ""):
        print "\nBlank message received. Discarding..."
    else:
        conn.send("Message received!")
        conn.close()
        print "\nNew message received!\n"
        print cipher.decrypt(msg, key)

