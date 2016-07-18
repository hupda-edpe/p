#!python

import requests

from pmucon.config import pm_config
from pmucon import pm_auth 

def get(endpoint):
  return request('get', endpoint)

def post(endpoint, payload):
  return request('post', endpoint, payload)

def put(endpoint):
  return request('put', endpoint)


def request(method, endpoint, payload=''):
  if endpoint and endpoint[0] is not '/': 
      endpoint = '/'+endpoint 
  url = pm_config.FULL_URL + endpoint

  if(method is 'get'):
    r = requests.get(url, headers=pm_auth.get_auth_hdr())
  elif(method is 'post'):
    r = requests.post(url, headers=pm_auth.get_auth_hdr(), data=payload)
  elif(method is 'put'):
    r = requests.put(url, headers=pm_auth.get_auth_hdr())
  else:
    raise Exception("No valid HTTP function was given. \"{method}\" Aborting." \
      .format(method = method))

  if r.status_code == 401:
    raise Exception("Bad login. Please check your login Info.")
  elif r.status_code != 200 and r.status_code != 201:
    err = "Error in {url}. The server replied: \n {code}: {msg}" \
      .format(url = endpoint, code=r.status_code, msg=r.json()['error'])
    raise Exception(err)
  else:
    try:
      return r.json()
    except:
      return r
