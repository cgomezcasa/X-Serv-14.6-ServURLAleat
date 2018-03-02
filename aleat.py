#!/usr/bin/python3

import webapp
import random

class urlAleatApp(webapp.webApp):
    def process(self, parsedRequest):
        return ("200 OK", "<html><body><h1><a href =" + 
                str(random.randint(1, 1000000)) + 
                "> Dame otra!</a></h1></body></html>")

if __name__ == "__main__":
    testWebApp = urlAleatApp("localhost", 1234)
