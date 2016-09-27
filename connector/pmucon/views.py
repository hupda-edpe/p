from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from pmucon import pm_wrapper, unicorn_wrapper


from pmucon.config import pm_config
from pmucon.models import *
import requests
import json

def index(req):
  return render(req, "pmucon/index.html")


def listStartCases(req):
  pm_token = req.session.get("pm_access_token")
  pmw = pm_wrapper.PMWrapper(pm_token)

  projects = pmw.getProjectList()

  for prj in projects:
    tasks = pmw.getStartingTasks(prj["pro_uid"])
    prj["tasks"] = tasks

  context = {
    "projects": projects
  }

  return render(req, "pmucon/start_cases.html", context)


    
@csrf_exempt
def catchMatch(req):
  print(req.body)
  jsn = json.loads(str(req.body, 'utf-8'))

  if 'A' in jsn:
    flat = {}
    a = jsn['A']
    b = jsn['B']
    for key in jsn.keys():
      for deep_key in jsn[key]:
        flat[deep_key] = jsn[key][deep_key]
    jsn = flat

  variables = {}
  for key in jsn.keys():
    if key != 'AppUid' and key != 'TasUid' and key != 'ProUid' and key != 'Timestamp':
      variables[key] = jsn[key]

  if 'AppUid' in jsn:
    app_uid = jsn['AppUid']
    case = get_object_or_404(Case, app_uid = app_uid)
    pm_wrapper.set_variables(case,variables)
    if not case.status == 'routed':
      pm_wrapper.route_case(case)
      case.status = 'routed'
      case.save()

  if 'TasUid' in jsn and 'ProUid' in jsn:
    pro_uid = jsn['ProUid']
    tas_uid = jsn['TasUid']
    app_uid = pm_wrapper.start_task(pro_uid, tas_uid)
    c = Case(app_uid=app_uid)
    pm_wrapper.set_variables(c, variables)
    pm_wrapper.route_case(c)

  return HttpResponse("")