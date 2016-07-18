#! python

import json

from pmucon.models import Case, CaseVariable
from pmucon import pm_rest

def pull_cases():
  cases = pm_rest.get('cases')
  for case in cases:
    if not Case.objects.filter(app_uid=case['app_uid']).exists():
      tas_uid = case['tas_uid']
      pro_uid = case['pro_uid']
      task = pm_rest.get('project/'+pro_uid+'/activity/'+tas_uid)
      props = json.loads(task['properties']['tas_description'])

      case_obj = Case(
        name    = case['app_tas_title'],
        app_uid = case['app_uid'],
        waiting = props['waiting'],
        event_type   = props['event_type'],
        status  = 'new')
      case_obj.save()

def route_case(case):
  endpoint = "/cases/{app_uid}/route-case".format(app_uid = case.app_uid)
  pm_rest.put(endpoint)

def get_variables(case):
  endpoint = '/cases/{app_uid}/variables'.format(app_uid = case.app_uid)
  return pm_rest.get(endpoint)

def set_variables(case, variables):
  endpoint = '/cases/{app_uid}/variable'.format(app_uid = case.app_uid)
  return pm_rest.put(endpoint, variables)

def start_task(pro_uid, tas_uid):
  payload = {
      "pro_uid": pro_uid,
      "tas_uid": tas_uid
  }
  r = pm_rest.post('cases', payload)
  return r["app_uid"]

class PMWrapper:
  """Wrapper-Class for the Processmaker API"""

  def pushInitial(self, uid):
    task = self.start_tasks[uid]

    case_uid = self.startCase(task)

    # put some required variables in case..

    return self.routeCase(case_uid)

  def pullIntermediate(self):
    cases = pm_rest.get('cases')

    for case in cases:
      if not Case.objects.filter(app_uid=case['app_uid']).exists():
        tas_uid = case['tas_uid']
        pro_uid = case['pro_uid']
        task = pm_rest.get('project/'+pro_uid+'/activity/'+tas_uid)
        props = json.loads(task['properties']['tas_description'])

        case_obj = Case(
          name    = case['app_tas_title'],
          app_uid = case['app_uid'],
          waiting = props['waiting'],
          event_type   = props['event_type'],
          status  = 'new')
        case_obj.save()

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
    r = pm_rest.get('project')
    # TODO Exception- and Error-Code-handling
    return [{"pro_uid": prj["prj_uid"], "name": prj["prj_name"] } for prj in r]

  def getStartingTasks(self, pro_uid):
    endpoint = "/project/{pro_uid}/starting-tasks".format(pro_uid=pro_uid)
    r = pm_rest.get(endpoint)
    # TODO Exception- and Error-Code-handling
    return [{"tas_uid": tsk["act_uid"], "name": tsk["act_name"], "pro_uid": pro_uid} for tsk in r]

  def startCase(self, task):
    payload = {
        "pro_uid": task["pro_uid"],
        "tas_uid": task["tas_uid"]
    }
    r = pm_rest.post('cases', payload)
    return r["app_uid"]

  def routeCase(self, app_uid):
    endpoint = "/cases/{app_uid}/route-case".format(app_uid = app_uid)
    r = pm_rest.put(endpoint)
    # TODO expect 200 and return True or False
    return r

if __name__ == "__main__":
  pmw = ProcessmakerWrapper()

  tasks = pmw.start_tasks
  example = tasks.keys()[0]
  # NOTE: The above shouldn't be the usual usecase.
  # When starting cases based on matched queries in unicorn,
  # the task/case id should either come from
  # manual mapping/configuration done beforehand or
  # or be derived from the matched query.

  pmw.pushInitial(example)
