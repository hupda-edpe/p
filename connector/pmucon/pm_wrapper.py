#! python

import requests
from pmucon.config import pm_config
from pmucon.models import PendingEvent
from pmucon import rest

class PMWrapper:
  """Wrapper-Class for the Processmaker API"""

  def __init__(self, auth_token):
    self.c = pm_config
    self.r = rest.Rest(self.c.FULL_URL)
    self.token = auth_token

  def pushInitial(self, uid):
    task = self.start_tasks[uid]

    case_uid = self.startCase(task)

    # put some required variables in case..

    return self.routeCase(case_uid)

  def pullIntermediate(self):
    cases = self.r.request("get", "/cases", None, self.token)

    for case in cases:
      if not PendingEvent.objects.filter(app_uid=case["app_uid"]).exists():
        pe = PendingEvent(app_uid=case["app_uid"], status="new")
        pe.save()

  def pushIntermediate(self, app_uid):
    # case_uid should be saved somewhere
    # also, case should be paused or in draft
    # set variables and stuff
    # maybe unpause case
    # route case
    pass

  def pullFinished(self):
    # seems to only work like pullIntermediate
    # -> task at the end of process, assigned to unicorn user
    pass


  def updateProcessData(self):
    prj_list = self.getProjectList()
    self.processes = {}
    self.start_tasks = {}
    for prj in prj_list:
      self.processes[prj["pro_uid"]] = prj
      tasks = self.getStartingTasks(prj["pro_uid"])
      for t in tasks:
        self.start_tasks[t["tas_uid"]] = t


  def getProjectList(self):
    r = self.r.request("get", "/project", None, self.token)
    # TODO Exception- and Error-Code-handling
    return [{"pro_uid": prj["prj_uid"], "name": prj["prj_name"] } for prj in r]

  def getStartingTasks(self, pro_uid):
    endpoint = "/project/{pro_uid}/starting-tasks".format(pro_uid=pro_uid)
    r = self.r.request("get", endpoint, None, self.token)
    # TODO Exception- and Error-Code-handling
    return [{"tas_uid": tsk["act_uid"], "name": tsk["act_name"], "pro_uid": pro_uid} for tsk in r]

  def startCase(self, task):
    payload = {
        "pro_uid": task["pro_uid"],
        "tas_uid": task["tas_uid"]
    }
    r = self.r.request("post", "/cases", payload, self.token)
    return r["app_uid"]

  def routeCase(self, app_uid):
    endpoint = "/cases/{app_uid}/route-case".format(app_uid = app_uid)
    r = self.r.request("put", endpoint, None, self.token)
    # TODO expect 200 and return True or False
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