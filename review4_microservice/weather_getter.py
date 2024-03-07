import requests
from cities import cities_tup

class WeatherGetter():
    def __init__(self, ):
        self.city_tup = cities_tup
    def getWeather(self, city):
        '''make a call for the weather'''
        try:
            w = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID=957d663a2296945e39a56609740a2548')
            return w.json()
        except Exception as err:
            print(f'Problem: {err}')

if __name__ == '__main__':
    wg = WeatherGetter()
    report = wg.getWeather('watford')
    print(report)

