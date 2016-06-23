#!python

import requests

class Rest(object):
    """Class for calling any PM REST endpoints."""

    def __init__(self, host):
        self.host = host

    def request(self, method, endpoint, data = "", access_token = ""):

        if not access_token:
            print "No valid access token given."
            return False

        if endpoint and endpoint[0] is not "/":
            endpoint = "/"+endpoint

        url    = self.host + endpoint
        header = {"Authorization": "Bearer {token}".format(token=access_token)}

        if(method is "get"):
            r = self.get(url, header)
        elif(method is "post"):
            r = self.post(url, header, data)
        elif(method is "put"):
            r = self.put(url, header)
        else:
            print "No valid HTTP function was given. \"{method}\" Aborting." \
                .format(method = method)
            return

        if r.status_code == 401:
            print "Bad login. Please check your login Info."
            return
        elif r.status_code != 200 and r.status_code != 201:
            print "Error in {host}. The server replied: \n {code}: {msg}" \
                .format(host = self.host, code=r.status_code, msg=r.json()["error"])
            return
        else:
            return r.json()

    def login(self, client_id, client_secret, username, password):
        url  = self.host + "/oauth2/token"
        header = None
        payload = {
            "grant_type":    "password",
            "scope":         "*",
            "client_id":     client_id,
            "client_secret": client_secret,
            "username":      username,
            "password":      password
        }
        r = requests.post(url, data = payload)
        if r.status_code != 200:
            print "Error in HTTP status code. {code}" \
                .format(code = r.status_code)
            return
        elif "error" in r.json():
            print "Error login in to PM server {host}. \n {err} \n {err_desc}" \
                .format(host = self.host, err = r.json()["error"], err_desc = r.json()["err_desc"])
            return
        else:
            return r.json()["access_token"]

    def get(self, url, header):
        return requests.get(url, headers=header)

    def post(self, url, header, payload):
        return requests.post(url, header, payload)

    def put(self, url, header):
        return requests.put(url, headers=header)
