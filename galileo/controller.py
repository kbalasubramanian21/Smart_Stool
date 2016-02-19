#!/usr/bin/python
import socket
import sys
import subprocess as sp
import time
from threading import Thread

# start a threaded process to grab the estimote data and dump it into a text file
bgthread = Thread(target = sp.call, args = ("hcitool lescan",), kwargs={"shell":True})
bgthread.setDaemon(True)
bgthread.start()
btthread = Thread(target = sp.call, args = ("./get_bluetooth_data.sh",), kwargs={"shell":True})
btthread.setDaemon(True)
btthread.start()

#from processdata import processData
HOST = '192.168.1.8'
PORT = 5002

# pin 7 (gpio 27) used for summon button
# pin 8 (gpio 26) used for dismiss button
sp.call('echo -n "27" > /sys/class/gpio/export',shell=True)
sp.call('echo -n "26" > /sys/class/gpio/export',shell=True)
sp.call('echo -n "in" > /sys/class/gpio/gpio27/direction',shell=True)
sp.call('echo -n "in" > /sys/class/gpio/gpio26/direction',shell=True)
sp.call('echo -n "pullup" > /sys/class/gpio/gpio27/drive',shell=True)
sp.call('echo -n "pullup" > /sys/class/gpio/gpio26/drive',shell=True)

# read pin 7:
def get_summon_val():
    return sp.check_output('cat /sys/class/gpio/gpio27/value',shell=True)
    
# read pin 8:
def get_dismiss_val():
    return sp.check_output('cat /sys/class/gpio/gpio26/value',shell=True)

# calculate position from estimote sensors
def calculate_location():
    # NEEDS IMPLEMENTATION    
    return (1,1)

# create message from come and location variable
def create_msg(come,location):
    return "COME " + str(int(come)) + "\nLOCATION " + str(location[0]) + " " + str(location[1]) + "\n"

come = False
location = (0,0)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (HOST, PORT)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# Wait for a connection
print >>sys.stderr, 'waiting for a connection'
connection, client_address = sock.accept()

endflag = 0

while True:
    print 1    

    print 2
    print >>sys.stderr, 'connection from', client_address

    # Receive the data in small chunks and retransmit it
    while True:
        summ = get_summon_val()
        dism = get_dismiss_val()
        # only change come if at least one of the buttons has been pressed
        if int(summ) or int(dism):
            if int(summ):
                come = True
            elif int(dism):
                come = False
        location = calculate_location()
        data = connection.recv(8096)
        print >>sys.stderr, 'received "%s"' % data
        if data:
            #processed_data = processData()
            print data
            print >>sys.stderr, 'sending data back to the client'
            msg = create_msg(come,location)
            connection.sendall(msg)
        else:
            print >>sys.stderr, 'no more data from', client_address
            endflag = 1
            break
    if endflag: 
        break

# Clean up the connection
print "closing connection"
connection.close()