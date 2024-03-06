import socket
import sys

def server():
    '''this microservice will listen for requests and respond
    It will be available over an http port (IP Internet Protocol)'''
    port_t = ('localhost', 9874) # any suitable IP address and port
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(port_t) # bind the socket to our IP settings
    # we can ask our server to listen
    server.listen()
    # we need a run loop
    while True:
        '''we need to keep running until we explicitly choose to break'''
        # if a request has been received, we can unpack the request
        (client, addr) = server.accept()
        print(f'Request received from {addr}')
        # break

if __name__ == '__main__':
    # start the server
    server()