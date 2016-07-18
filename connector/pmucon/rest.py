#!python

import requests

def get(url, hdr):
  return request('get', url, hdr)

def post(url, hdr, payload):
  return request('post', url, hdr, payload)

def put(url, hdr):
  return request('put', url, hdr)


def request(method, url, hdr, payload=""):
  if(method is "get"):
    r = requests.get(url, headers=hdr)
  elif(method is "post"):
    r = requests.post(url, headers=hdr, data=payload)
  elif(method is "put"):
    r = requests.put(url, headers=hdr)
  else:
    raise Exception("No valid HTTP function was given. \"{method}\" Aborting." \
      .format(method = method))

  if r.status_code == 401:
    raise Exception("Bad login. Please check your login Info.")
  elif r.status_code != 200 and r.status_code != 201:
    err = "Error in {url}. The server replied: \n {code}: {msg}" \
      .format(host = self.host, code=r.status_code, msg=r.json()["error"])
    raise Exception(err)
  else:
    try:
      return r.json()
    except:
      return r
