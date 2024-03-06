import socket
import sys
import datetime

def writreToFile(data, filename):
    '''we can log activity to a file'''
    ds = datetime.datetime.now()
    try:
        with open(filename, 'a') as fout:
            fout.write(f'on {ds} received {data}\n')
            # with will close the file access object when done
    except Exception as err:
        print(err)

def server():
    '''this microservice will listen for requests and respond
    It will be available over an http port (IP Internet Protocol)'''
    port_t = ('localhost', 9874) # any suitable IP address and port
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(port_t) # bind the socket to our IP settings
    # we can ask our server to listen
    server.listen(4) # backlog up to 4 clients
    print(f'Server is listening on {port_t[0]} port {port_t[1]}')
    filename = 'serverlog.txt' # this could be dynamically generated
    # we need a run loop
    while True:
        '''we need to keep running until we explicitly choose to break'''
        # if a request has been received, we can unpack the request
        (client, addr) = server.accept()
        # we typically read the first part of a request
        buf = client.recv(1024) # just the first 1024 bytes
        writreToFile(f'{buf}', filename)
        print(f'Request received from {addr} {buf}')
        if buf==b'quit':
            server.close() # we should tidy up!
            break
        # we may choose to respond to the client
        client.send( buf.upper()) # respond with an upper-case version of the request
        client.close() # tidy up - release resource


if __name__ == '__main__':
    # start the server
    server()