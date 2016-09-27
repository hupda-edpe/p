""" This module is a simple wrapper for calling the ProcessMaker API.
Connection details are extracted from config/pm_config.py and authentication
is done via the pm_auth module.
Some errorhandling is provided, but sane return values aren't guaranteed.

"""

import requests

from pmucon.config import pm_config
from pmucon import pm_auth 

def get(endpoint):
  """HTTP GET wrapper for the request function."""
  return request('get', endpoint)

def post(endpoint, payload):
  """HTTP POST wrapper for the request function."""
  return request('post', endpoint, payload)

def put(endpoint, payload=''):
  """HTTP PUT wrapper for the request function."""
  return request('put', endpoint, payload)


def request(method, endpoint, payload=''):
  """ Perform a request to ProcessMaker.

  Args:
    method -- The HTTP request method to be used.
    endpoint -- The endpoint of the PM API to be called.
    payload -- Will be sent as content when using POST or PUT methods.

  Returns:
    If the response is a json it will be converted into a dict and returned.
    Otherwise the plain content of the response will be returned.
  """
  if endpoint and endpoint[0] is not '/': 
      endpoint = '/'+endpoint 
  url = pm_config.FULL_URL + endpoint

  if(method is 'get'):
    r = requests.get(url, headers=pm_auth.get_auth_hdr())
  elif(method is 'post'):
    r = requests.post(url, headers=pm_auth.get_auth_hdr(), data=payload)
  elif(method is 'put'):
    r = requests.put(url, headers=pm_auth.get_auth_hdr(), data=payload)
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
