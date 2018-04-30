import os

ssler = ""

command = raw_input("GET, HEAD, POST? ")
dest = raw_input("IP or web address? ")
port = raw_input("Port? ")
sslify = raw_input("Use SSL? ")
if sslify == "y":
    ssler = "--ssl"

action = "printf '%s / HTTP/1.1\r\nHost: %s\r\n\r\n' | ncat %s %s %s"%(command,dest,ssler,dest,port)

raw_input("\n--------\nYou will run:\n---------\n" + action + "\n---------\nPress ENTER to continue.")

os.system(action)
