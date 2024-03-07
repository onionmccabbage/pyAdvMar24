import socket
import sys

class MicroClient():
    def __init__(self):
        '''if there are system argumetn variables, use them
        otherwise send a default message'''
        if len(sys.argv)>1: 
            self.msg = ' '.join(sys.argv[1:]) # combine the system args into a string
        else:
            self.msg = 'default'
    def MyClient(self):
        '''make requests to our microservice'''
        cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # must match server
        config_t = ('localhost', 9874) # IP and port
        cli.connect(config_t)
        # send a message ot the server
        msg = self.msg
        cli.send(msg.encode()) # we are obliged to encode anything passed over http
        # we can choose to handle any respoinse from the server
        response = cli.recv(1024)
        print(f'Client received {response}') # bytes
        cli.close() # a good idea to tidy up

if __name__ == '__main__':
    c = MicroClient()
    c.MyClient() # our client is running