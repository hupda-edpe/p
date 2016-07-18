from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse


from pmucon import pm_wrapper, unicorn_wrapper


from pmucon.config import pm_config
from pmucon.models import Case, Event, EventVariable
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
  j = json.loads(req.body)

  if PendingEvent.objects.filter(app_uid=j["AppUid"]).exists():
    pe = PendingEvent.objects.get(app_uid=j["AppUid"])
    pe.delete()

  ok, pm_token = genAuthTok(req)
  pmw = pm_wrapper.PMWrapper(pm_token)

  r = pmw.routeCase(j["AppUid"])


  return HttpResponse("")