from datetime import datetime
now = str(datetime.now())

def addTimestamp(function):
    def newFunction(string):
        return function(string + " " + now)
    return newFunction