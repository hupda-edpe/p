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
  jsn = json.loads(req.body)

  if jsn['Mode'] == 'App':
    app_uid = jsn['AppUid']
    case = get_object_or_404(Case, app_uid = app_uid)
    if not case.status == 'routed'
      pm_wrapper.route_case(case)
      case.status = 'routed'
      case.save()
  elif: jsn['Mode'] == 'Task':
    pro_uid = jsn['ProUid']
    tas_uid = jsn['TasUid']
    pm_wrapper.start_task(pro_uid, tas_uid)

  return HttpResponse("")