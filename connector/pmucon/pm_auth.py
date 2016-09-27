#! Python

import requests, os, json, time

from pmucon.config import pm_config

"""
The tokenfile has following syntax:

{
  "access_token": "f0ac828ac4d3cbcbba470bb7b190c827c5e959f2",
  "refresh_token": "7d880ab5ac0255fe1f9ae3323698e7de64e9bb02",
  "expires_at": 86400
}
"""

def get_auth_hdr():
  tok = get_token()
  return {"Authorization": "Bearer {token}".format(token=tok)}

def get_token():
  token_info = parse_token_info()
  
  if token_info == None:
    token_info = generate_new_token()
    save_token_info(token_info)

  if token_info["expires_at"] < time.time():
    token_info = refresh_token(token_info)
    save_token_info(token_info)

  return token_info["access_token"]


def parse_token_info():
  if not os.path.exists('tokenfile.txt'):
    return None
  with open('tokenfile.txt', 'r') as f:
    jsn = json.loads(f.read())
  return jsn

def save_token_info(token_info):
  with open('tokenfile.txt', 'w') as f:
    f.write(json.dumps(token_info))


def refresh_token(token_info):
  c = pm_config
  url  = c.API_PROTOCOL + c.PM_HOST + '/' + c.PM_WORKSPACE + "/oauth2/token"
  payload = {
    "grant_type":    "refresh_token",
    "client_id":     c.CLIENT_ID,
    "client_secret": c.CLIENT_SECRET,
    "refresh_token": token_info["refresh_token"]
  }
  r = requests.post(url, data = payload)
  r.raise_for_status()
  jsn = r.json()

  if "error" in jsn:
    errormsg = "Error while refreshing token. PM server {host}. <br> {err} <br> {err_desc}" \
          .format(host = url, err = jsn["error"], err_desc = jsn["err_desc"])
    raise Exception(errormsg)

  token_info["access_token"] = jsn["access_token"]
  token_info["expires_at"] = time.time() + jsn["expires_in"]
  return token_info

def generate_new_token():
  c = pm_config
  url  = c.API_PROTOCOL + c.PM_HOST + '/' + c.PM_WORKSPACE + "/oauth2/token"
  payload = {
    "grant_type":    "password",
    "scope":         "*",
    "client_id":     c.CLIENT_ID,
    "client_secret": c.CLIENT_SECRET,
    "username":      c.PM_USER,
    "password":      c.PM_PW
  }
  r = requests.post(url, data = payload)
  r.raise_for_status()
  jsn = r.json()

  if "error" in jsn:
    errormsg = "Error login in to PM server {host}. <br> {err} <br> {err_desc}" \
          .format(host = url, err = jsn["error"], err_desc = jsn["err_desc"])
    raise Exception(errormsg)

  token_info = {
    "access_token": jsn["access_token"],
    "refresh_token": jsn["refresh_token"],
    "expires_at": time.time() + jsn["expires_in"]
  }
  return token_info