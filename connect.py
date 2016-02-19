import socket
import sys
import time
import rospy

HOST = '192.168.1.8'
PORT = 5002

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (HOST, PORT)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

numTimes = 100

for i in range(numTimes):

    # Send data
    message = 'ETA '
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    data = sock.recv(8096)
#        amount_received += len(data)
    print >>sys.stderr, 'received: \n', data

    time.sleep(1)


print >>sys.stderr, 'closing socket'
sock.close()

