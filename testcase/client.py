#! python

import requests

"http://wiki.processmaker.com/3.0/Triggers#Enabling_Debug_Mode"

# TODO: Retrieve constants from external config file

PM_HOST      = "172.17.0.3"
PM_WORKSPACE = "workflow"

PM_USER = "unicorn"
PM_PW   = "123456"

CLIENT_ID     = "UCYFOVTKROBJVFWYBWJRQIPWFUNBZCAT"
CLIENT_SECRET = "189803135575f01c37fb0b7099422018"

def  getAccessToken():
  url = "http://{host}/{workspace}/oauth2/token".format(host=PM_HOST, workspace=PM_WORKSPACE)
  payload = {
    "grant_type": "password",
    "scope": "*",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "username": PM_USER,
    "password": PM_PW
  }
  r = requests.post(url, data=payload)

  # Stop if status isn't 200 OK
  r.raise_for_status()

  jsn = r.json()

  if "error" in jsn:
    print (jsn)
    return
  else:
    return r.json()


def getProjectsList():
    "http://wiki.processmaker.com/3.0/REST_API_Designer#get_projects"

def getStartingTasks():
    "http://wiki.processmaker.com/3.0/REST_API_Designer#Get_starting_tasks"


def startCase(access, pro_uid, tas_uid):
  url = "http://{host}/api/1.0/{workspace}/cases".format(host=PM_HOST, workspace=PM_WORKSPACE)
  auth = {"Authorization": access["access_token"]}
  payload = {
    "pro_uid": pro_uid,
    "tas_uid": tas_uid
  }
  r = requests.post(url, headers=auth, data=payload)
  return r

def routeCase(access, app_uid):
  url = "http://{host}/api/1.0/{workspace}/cases/{app_uid}/route-case"
    .format(host=PM_HOST, workspace=PM_WORKSPACE, app_uid=app_uid)
  auth = {"Authorization": access["access_token"]}
  r = requests.put(url, headers=auth, data=payload)
  return r

if __name__ == "__main__":
  print("this is a lib module")