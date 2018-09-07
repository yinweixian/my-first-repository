#made by !/usr/bin/pythonRoot
#copyd my matthew walker
#bring in the liraries
import RPi.GPIO as G
from flup.server.fcgi import WSGIServer
import sys, urlparse

#set up our GPIO pins
G.setmode(G.BCM)
G.setup(4, G.OUT)
G.setup(17, G.OUT)
G.setup(22, G.OUT)

# all of our code now lives within the app() function whic is called for each http request we recieve
def app(environ, start_response):
    #start our http response
    start_response("200 OK", [("Content-Type", "text/html")])
    #look for inputs on the URL
    i = urlparse.parse_qs(environ["QUERY_STRING"])
    yield ('&nbsp;') # flup expects a string to be returned from this function
    #if there's a url variable named 'q'
    if "r" in i:
        if i["r"][0] == "w":
            g.output(4, True)  #turn it on
        elif i["r"][0] == "s":
            G.output(17, False) #turn it off

    if "y" in i:
        if i["y"][0] == "w":
            G.output(17, True) #turn it on
        elif i["y"][0] == "s":
            G.output(17, False) #turn it off

    if "g" in i:
        if i["g"][0] == "w":
            G.output(22, True) #turn it on
        elif i["g"][0] == "s":
            G.output(22, False) #turn it off

#by default, flup works out how to bind to the web server for us, so just call it with our app() function and let it get on with it
WSGIServer(app).run()
