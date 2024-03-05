'''We will access data from https://jsonplaceholder.typicode.com/photos  '''
# we will need the 'requests' library
# pip install requests
# pip3 install requests
# python -m pip install requests
import requests
apiURL = 'https://jsonplaceholder.typicode.com/photos' # this returns JSON for photos

def getData():
    ''' fetch some data from an API end point'''
    # we can call get, post, put, update, delete for the API
    global apiURL # we now have access to the asset in the global namespace
    response_obj = requests.get(apiURL) # we now have a response object
    r = genericUtil(response_obj)
    return r

def getOnePhoto(n): # we should validate n
    '''Fetch just a single photo based on id=n'''
    global apiURL # be careful - we might not want to polute the global namespace
    response_obj = requests.get( f'{apiURL}/{n}' )
    r = genericUtil(response_obj)
    return r

def genericUtil(response_obj):
    res_j = response_obj.json() # or .text() .html() etc.
    return res_j

if __name__ == '__main__':
    photos = getData()
    print(photos) # we have a (very large) list
    photo = getOnePhoto(3)
    print(f'Photo 3 is {photo}')