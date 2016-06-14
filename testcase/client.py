#! python

import requests
import config

class ProcessmakerWrapper:
  """Wrapper-Class for the Processmaker API"""

  def __init__(self, config):
    self.c = config
    self.base_url = "http://{host}/api/1.0/{workspace}" \
      .format(host=self.c.PM_HOST, workspace=self.c.PM_WORKSPACE)
    self.auth = self.genAuthHeader():
    self.updateProcessData()

  def pushInitial(self, uid):
    task = self.start_tasks[uid]

    case_uid = self.startCase(task)

    # put some required variables in case..

    self.routeCase(case_uid)

  def pullIntermediate(self):
    # get case inbox (GET /cases)
    # is there some?
    # -> save app_uid somewhere
    # get variables and stuff
    # send id, variables etc to unicorn
    # (maybe) pause case (PUT /cases/app_uid/pause)
    # or send to draft (happens automatically,
    # when some step of current task in case is completed)

  def pushIntermediate(self, case_uid):
    # case_uid should be saved somewhere
    # also, case should be paused or in draft
    # set variables and stuff
    # maybe unpause case
    # route case

  def pullFinished(self):
    # seems to only work like pullIntermediate
    # -> task at the end of process, assigned to unicorn user


  def genAuthHeader(self):
    jsn = self.getAccessToken()
    if "error" in jsn:
      print(jsn)
      return
    else:
      return {"Authorization": "Bearer {tok}".format(tok=jsn["access_token"])}

  def  getAccessToken(self):
    url = "http://{host}/{workspace}/oauth2/token" \
      .format(host=self.c.PM_HOST, workspace=self.c.PM_WORKSPACE)
    payload = {
      "grant_type": "password",
      "scope": "*",
      "client_id": self.c.CLIENT_ID,
      "client_secret": self.c.CLIENT_SECRET,
      "username": self.c.PM_USER,
      "password": self.c.PM_PW
    }
    r = requests.post(url, data=payload)
    # Stop if status isn't 200 OK
    r.raise_for_status()
    return r.json()

  def updateProcessData(self):
    prj_list = self.getProjectList()
    self.processes   = {}
    self.start_tasks = {}
    for prj in prj_list:
      self.processes[prj["uid"]] = prj
      tasks = self.getStartingTasks(prj["uid"])
      for t in tasks:
        self.start_tasks[t["uid"]] = t

  def getProjectList(self):
    url = "{base}/project".format(base=self.base_url)
    r = requests.get(url, headers=self.auth)
    # TODO Exception- and Error-Code-handling
    return [{"uid": prj["prj_uid"], "name": prj["prj_name"] } for prj in r.json()]

  def getStartingTasks(self, process_uid):
    url = "{base}/project/{prj_uid}/starting-tasks" \
      .format(base=self.base_url, prj_uid=process_uid)
    r = requests.get(url, headers=self.auth)
    # TODO Exception- and Error-Code-handling
    return [{"uid": tsk["act_uid"], "name": tsk["act_uid"], "process": process_uid} for tsk in r.json()]

  def startCase(self, task):
    url = "{base}/cases".format(base=self.base_url)
    payload = {
      "pro_uid": task["process"],
      "tas_uid": task["uid"]
    }
    r = requests.post(url, headers=self.auth, data=payload)
    return r.json()["app_uid"]

  def routeCase(self, case_uid):
    url = "{base}/cases/{app_uid}/route-case" \
      .format(base=self.base_url, app_uid=case_uid)
    r = requests.put(url, headers=self.auth)
    return r

if __name__ == "__main__":
  pmw = ProcessmakerWrapper(config)

  tasks = pmw.start_tasks
  example = tasks.keys()[0]
  # NOTE: The above shouldn't be the usual usecase.
  # When starting cases based on matched queries in unicorn,
  # the task/case id should either come from
  # manual mapping/configuration done beforehand or
  # or be derived from the matched query.

  pmw.pushInitial(example)