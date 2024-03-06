from flask import Flask # may need to python -m pip install flask

# for small microservices, build your own
# for medium server use flask
# for fully featured web content management use django (all free)

app = Flask(__name__)

# we declare http 'RESTful' routes for our flask API
@app.route('/') # this is the root of our service
def root():
    '''here we present content available at the root of our web api'''
    return 'welcome to the flask server' # Flask will handle any encoding

# we may declare many routes
@app.route('/info') # the url will be https://127.0.0.1:5000/info
def info():
    content = '<h2>Information Page</h2>'
    return content

# here is some JSON
@app.route('/penguin')
def penguin():
    # we might access teh data from a database, based on the request parameters in the URL
    p_j = ({"creature":"penguin", "count":12, "cost":0.52}) # anything but a list!!
    return p_j # Flask will take care of making this into text

# it is common to provide several routes to the same end point
@app.route('/aluminium')
@app.route('/aluminum')
@app.route('/allumineum')
@app.route('/al')
def al():
    return 'the correct spelling is aluminium'

# we can access any parts of the RESTful url




if __name__ == '__main__':
    app.run() # start the Flask server in a run loop
