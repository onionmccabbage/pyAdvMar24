# a service to access https://swapi.co/api
import requests

class SwapiService(object):
    def __init__(self):
        pass
    @staticmethod
    def getSwapi(category, id): # no need for self this time (since its a static method)
        url = f"https://swapi.info/api/{category}/{id}"
        print(url)
        response = requests.get(url)
        return response.text

if __name__ == "__main__":
    # SwapiService().__init__()
    swapi = SwapiService()
    p = swapi.getSwapi('people', 1)
    print(p)