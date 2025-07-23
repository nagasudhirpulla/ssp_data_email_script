# import json module
import json

# initialize the app config global variable
appConf = {}
pointsConf = {}


def loadAppConfig(fName="secret/config.json"):
    # load config json into the global variable
    with open(fName) as f:
        global appConf
        appConf = json.load(f)
        return appConf


def loadPoints(fName="secret/points.json"):
    # load config json into the global variable
    with open(fName) as f:
        global pointsConf
        pointsConf = json.load(f)
        return pointsConf


def getAppConfig():
    # get the cached application config object
    global appConf
    return appConf


def getPoints():
    # get the cached application config object
    global pointsConf
    return pointsConf
