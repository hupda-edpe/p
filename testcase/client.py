#! python

import requests

from config import *

# General


def genAuthHeader():
  jsn = getAccessToken()
  if "error" in jsn:
    print(jsn)
    return
  else:
    return {"Authorization": "Bearer {tok}".format(tok=jsn["access_token"])}

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
  return r.json()


# Starting New Case

def getProjectsList(auth):
  url = "http://{host}/api/1.0/{workspace}/project".format(host=PM_HOST, workspace=PM_WORKSPACE)
  r = requests.get(url, headers=auth)
  return r.json()

def getStartingTasks(auth, prj):
  url = "http://{host}/api/1.0/{workspace}/project/{prj_uid}/starting-tasks" \
    .format(host=PM_HOST, workspace=PM_WORKSPACE, prj_uid=prj["prj_uid"])
  r = requests.get(url, headers=auth)
  return r.json()

def listProjects(jsn):
  print("UID                              | Name")
  for proj in jsn:
    print("{uid} | {name}".format(uid=proj["prj_uid"], name=proj["prj_name"]))

def listTasks(jsn):
  print("UID                              | Name")
  for tsk in jsn:
    print("{uid} | {name}".format(uid=tsk["act_uid"], name=tsk["act_name"]))

def listAllStartingTasks(auth):
  pl = getProjectsList(auth)
  for prj in pl:
    print("\n\nProject:\n{uid} | {name}\n".format(uid=prj["prj_uid"], name=prj["prj_name"]))
    st = getStartingTasks(auth, prj)
    listTasks(st)


def startCase(auth, pro_uid, tas_uid):
  url = "http://{host}/api/1.0/{workspace}/cases".format(host=PM_HOST, workspace=PM_WORKSPACE)
  payload = {
    "pro_uid": pro_uid,
    "tas_uid": tas_uid
  }
  r = requests.post(url, headers=auth, data=payload)
  return r

def routeCase(auth, app_uid):
  url = "http://{host}/api/1.0/{workspace}/cases/{app_uid}/route-case" \
    .format(host=PM_HOST, workspace=PM_WORKSPACE, app_uid=app_uid)
  r = requests.put(url, headers=auth)
  return r

if __name__ == "__main__":
  print("this is a lib module")