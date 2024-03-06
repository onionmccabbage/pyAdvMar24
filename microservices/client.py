# we can make a socket client
import socket
import sys
def client():
    '''this is a simple socket client to interact with our socket server'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_t = ('localhost', 9874)
    # we can try to connect to our server
    client.connect(port_t)

    # we can send a request to our server
    client.send('info'.encode()) # all http traffic must be encoded

if __name__ == '__main__':
    client()