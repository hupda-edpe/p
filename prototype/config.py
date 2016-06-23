#! Python

import json


class Config:
    """OO-Style config file"""

    def __init__(self):
        self.readConfigFile()

    def readConfigFile(self):
        with open('config.json') as config_file:
            config = json.load(config_file)
        for key, value in config.iteritems():
            setattr(self, key, value)

    def getHost(self):
        return self.PM_HOST

    def getWorkspace(self):
        return self.PM_WORKSPACE

    def getUser(self):
        return self.PM_USER

    def getPassword(self):
        return self.PM_PW

    def getClientId(self):
        return self.CLIENT_ID

    def getClientSecret(self):
        return self.CLIENT_SECRET

    def getUrl(self):
        return self.API_PROTOCOL + self.getHost(
        ) + self.API_URL + "/" + self.getWorkspace()
