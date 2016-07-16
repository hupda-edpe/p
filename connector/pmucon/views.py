from django.shortcuts import render
from django.http import HttpResponse


from pmucon import pm_wrapper, unicorn_wrapper
from pmucon.config import pm_config
from pmucon.models import PendingEvent
import requests
import json

def index(req):
  context = {
    "pm_access_token": req.session.get("pm_access_token")
  }

  return render(req, "pmucon/index.html", context)

def pmAuth(req):
  ok, data = genAuthTok(req)

  if ok:
    context = {
      "ok": ok,
      "token": data
    }
  else:
    context = {
      "ok": ok,
      "errormsg": data
    }

  return render(req, "pmucon/pm_auth.html", context)

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

def pullCases(req):
  pm_token = req.session.get("pm_access_token")
  pmw = pm_wrapper.PMWrapper(pm_token)

  pmw.pullIntermediate()

  context = {
    "events": PendingEvent.objects.all
  }

  return render(req, "pmucon/pull_cases.html", context)

def pushCase(req):
  pass

def postEventType(req):
  pass

def postEvent(req, app_uid):
  ok = False
  if PendingEvent.objects.filter(app_uid=app_uid).exists():
    pe = PendingEvent.objects.get(app_uid=app_uid)
    if pe.status == "new" or pe.status == "posted":
      pe.status = "posted"
      pe.save()
      unicorn_wrapper.postEvent(app_uid)
      ok = True
  return render(req, "pmucon/post_event.html", {"ok": ok})


def routeCase(req, app_uid):
  pm_token = req.session.get("pm_access_token")
  pmw = pm_wrapper.PMWrapper(pm_token)

  r = pmw.routeCase(app_uid)

  return HttpResponse("routed")



def deleteCases(req):
  for pe in PendingEvent.objects.all():
    pe.delete()


  return HttpResponse("deleted")

def genAuthTok(req):
  c = pm_config

  url  = c.FULL_URL + "/oauth2/token"
  payload = {
    "grant_type":    "password",
    "scope":         "*",
    "client_id":     c.CLIENT_ID,
    "client_secret": c.CLIENT_SECRET,
    "username":      c.USER,
    "password":      c.PW
  }

  r = requests.post(url, data = payload)

  if r.status_code != 200:
    errormsg = "Error in HTTP status code. {code}" \
          .format(code = r.status_code)
    ok = False
  elif "error" in r.json():
    errormsg = "Error login in to PM server {host}. <br> {err} <br> {err_desc}" \
          .format(host = url, err = r.json()["error"], err_desc = r.json()["err_desc"])
    ok = False
  else:
    token = r.json()["access_token"]
    ok = True
    req.session["pm_access_token"] = token

  if ok:
    return (ok, token)
  else:
    return (ok, errormsg)