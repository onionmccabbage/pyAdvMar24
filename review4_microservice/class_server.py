import socket # this lets us make clients and services
from cities import cities_tup
from weather_class import Weather
from weather_getter import WeatherGetter
import json

class MicroServer():
    '''a server which responds to requests'''
    def __init__(self, config=('localhost', 9874)): # we expect a tuple
        # we can validate the incoming config
        self.config = config
        # self.weatherGetter = WeatherGetter or use a global isntance
    @property
    def config(self):
        return self.__config 
    @config.setter
    def config(self, new_config):
        '''must be a tuple containing a non-empty string and a positive integer'''
        if type(new_config)==tuple and type(new_config[0])==str and new_config[0]!='' and type(new_config[1])==int and new_config[1]>0:
            self.__config = new_config
        else:
            raise TypeError('the configuration is wrong')            
    def MyServer(self):
        '''This microservice will receive request from clients'''
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        config_t = self.__config
        server.bind(config_t) # our server knows which IP address and port is should use
        # we can make a judgement as to how manyclients we might handle
        server.listen(4) # our server begins listening for requests
        # we need our serve to continue indefinitely - a run loop
        while True:
            # begin responding  to requests
            (client, addr) = server.accept()
            # print(client, addr) # not actually useful - except debug
            # echo back whatever the client sent as an upper-case string
            buf = client.recv(1024) # the first 1024 bytes of the request
            req = buf.decode()
            if req == 'quit':
                break
            # do we have an acceptable city name?
            if req in cities_tup:
                data = wg.getWeather(req) # use a global instance of the WeatherGetter class
                # make a weather model instance
                lat = data['coord']['lat']
                lon = data['coord']['lon']
                tem = data['main']['temp']
                w = Weather(lat, lon, tem) # we have an instance of a weather model
                # now send a nice string back to the client
                w_d = json.dumps(w.__dict__)
                w_s = f'lat:{w.lat} lon:{w.lon} temp:{w.temperature}'
                resp = w_d
            else:
                resp = buf.decode().upper() # force to upper case
                print(f'Server received {buf} and will send {resp}')
            client.send(resp.encode())

if __name__ == '__main__':
    wg = WeatherGetter()
    s = MicroServer() # we could inject a config tuple
    s.MyServer() # the server is now running