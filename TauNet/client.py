#This is the client program for the TauNet system.
#Copyright (c) 2015 Matthew Tighe 

#import cipher
import csv, socket, os, cipher

version = "0.2"
me = "mattTighe"
port = 6283

def displayUserList():
    with open('userlist.csv', 'r') as f:
        reader = csv.reader(f)
        i = 0
        userList = []
        for row in reader:
            if i == 0:
                print "   " + str(row)
                i += 1
                userList.append(str(row))
            else:
                print str(i) + ": " + str(row)
                i += 1
                userList.append(str(row))

        return userList


def createMsg(header):
    tooLong = 1
    
    while tooLong != 0:
        msg = header + input("Please enter the message you would like to send, entered within quotes: ")
        if len(msg) > 934:
            print ("Your message is too long. Please restrict messages to" 
            "1kb in length, which should be no more than 934 characters")
        else:
            tooLong = 0

    return msg

def send(msg, domain):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #this removes the single quotes surround the string
    domain = domain[2:-1]
    s.connect((domain, port))
    s.send(msg)


def Main():
    keycheck = "password"
    menuOption = "0"
    
    print ("Welcome to the TauNet client program!\n"
            "Please note: Any input to the system must be surrounded by quotes\n")
    key = input("Please enter your TauNet key: ")
    
    while(keycheck != key):
        print "That is an incorrect key.\n"
        key = input("Please try again or enter Q to quit: ")
        if key == "Q":
            menuOption = "Q"
            print "Thanks for using TauNet!"
            break

    while(menuOption != "Q"):
        menuOption = input(("What would you like to do?\n"
                            "1: Message a user\n"
                            "Q: Quit\n"))
        if menuOption == "Q":
            print "Thanks for using TauNet!\n"
            break
        elif menuOption == "1":
            userList = displayUserList()
            msgOption = input(("Enter the number corresponding to the user you "
                                "would like to message: "))
            
            #this separates the user and domain from the entire row of the userlist.csv
            parser = userList[int(msgOption)]
            user = parser.split(',')[0]
            user = user[1:]
            domain = parser.split(',')[1]

            header = "version: " + version + "\r\nfrom: " + me + "\r\nto: " + user[1:-1] + "\r\n\r\n"

            msg = createMsg(header)
            msg = cipher.encrypt(msg, key)
            send(msg, domain)

        else:
            "Invalid choice. Please try again.\n"


Main()
