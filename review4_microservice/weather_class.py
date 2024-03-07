class Weather():
    def __init__(self, lat, lon, temperature):
        self.lat = lat
        self.lon = lon
        self.temperature = temperature
    @property
    def lat(self):
        return self.__lat
    @lat.setter
    def lat(self, new_lat):
        if type(new_lat) in (int, float):
            self.__lat = new_lat
        else:
            self.__lat = 0 # default
    @property
    def lon(self):
        return self.__lon
    @lon.setter
    def lon(self, new_lon):
        if type(new_lon) in (int, float):
            self.__lon = new_lon
        else:
            self.__lon = 0 # default
    @property
    def temperature(self):
        return self.__temperature
    @temperature.setter
    def temperature(self, new_temperature):
        if type(new_temperature) in (int, float):
            self.__temperature = new_temperature
        else:
            self.__temperature = 12 # default
    def __str__(self):
        return f'lat:{self.lat} lon:{self.lon} temperature:{self.temperature}'

if __name__ == '__main__':
    w = Weather(1.2, 2.1, 13)
    # duck typing - if it looks and behaves like a duck - its a duck!!
    other = {'lat':0.0, 'lon':0.0, 'temperature':12}
    print(w)
