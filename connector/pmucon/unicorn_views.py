from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from pmucon.models import *

from pmucon import unicorn_wrapper

import requests
import json

def list_event_types(req):
  context = {
    "event_type_list" = EventType.objects.all()
  }

  return render(req, "pmucon/unicorn/list_event_types.html", context)


def event_type(req, et_id):
  et = get_object_or_404(EventType, pk=et_id)

  pass

def new_event_type_element(req, et_id)
  


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