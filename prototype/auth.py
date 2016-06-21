#! python

import requests
import config
import os

class Auth:
    """Authentication for PMWrapper"""

    def __init__(self, config):
        self.c = config

    def retrieveAccessToken(self, app):
        """Retrieves a previously stored acces token for the specified app."""
        tokens = self.read("tokens")
        token = tokens[app]

        # TODO
        # error handling


    def storeAccessToken(self, app, token):
        """Writes a combination of app name and access token as dict in external file."""
        db = self.read("tokens")
        new = {app: token}
        tmp = db.copy()
        tmp.update(new)
        self.write("tokens", tmp)

        # TODO
        # re-retrieve to check if it worked
        # error handling
        # Special feature: Encrypt file

    def getAccessToken(self):
        # TODO
        # copy from client.py

    def validateAccessToken(self):
        # TODO
        # check if access_token is valid for app

    def genAuthHeader(self):
        # TODO
        # copy from client.py

################################################################################
###                              HELPER METHODS                              ###
################################################################################
    def file_exists(self,filename):
        try:
            if os.stat(filename).st_size > 0:
               return True
            else:
               return True
        except OSError:
            return False

    def read(self,filename):
        if(not file_exists(filename)):
            return False
        with open(filename, 'r') as f:
            f = f.read()
            if(f == ''):
                return ""
            else:
                return eval(f)

    def write(self,filename, content):
        f = open(filename, "r+")
        f.write(str(content))
        f.close
