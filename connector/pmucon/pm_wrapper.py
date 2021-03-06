"""This module provides a simple interface for communicating with ProcessMaker
in a way that is needed throughout this django application.
"""

import json

from pmucon.models import Case, CaseVariable
from pmucon import pm_rest

def pull_cases():
  """Pull all open cases (tasks) for the unicorn user from ProcessMaker and save
  new ones into the database.
  """
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
        blocking = props['blocking'],
        event_type   = props['event_type'],
        status  = 'new')

      if 'start_task' in props and 'start_process' in props:
        case_obj.tas_uid = props['start_task']
        case_obj.pro_uid = props['start_process']
      case_obj.save()

def route_case(case):
  """Route a given case in PM. Which essentially means marking the current
  task as done and letting the underlying process continue.
  """
  endpoint = "/cases/{app_uid}/route-case".format(app_uid = case.app_uid)
  pm_rest.put(endpoint)

def get_variables(case):
  """Get case variables of given case."""
  endpoint = '/cases/{app_uid}/variables'.format(app_uid = case.app_uid)
  return pm_rest.get(endpoint)

def set_variables(case, variables):
  """Set case variables of given case."""
  endpoint = '/cases/{app_uid}/variable'.format(app_uid = case.app_uid)
  return pm_rest.put(endpoint, variables)

def start_task(pro_uid, tas_uid):
  """Start a new task (instance of a process).

  Returns the app_uid of the started task.
  """
  payload = {
      "pro_uid": pro_uid,
      "tas_uid": tas_uid
  }
  r = pm_rest.post('cases', payload)
  return r["app_uid"]


class PMWrapper:
  """An obsolete wrapper class for ProcessMaker.

  This was used in the prototype but doesn't fulfill any purpose at the moment.
  It rests here in case some of its functionality is needed again and also to 
  document the origins of the ProcessMaker-Unicorn-Connector.
  """

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