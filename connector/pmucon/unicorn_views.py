from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from pmucon.models import *

from pmucon import unicorn_wrapper

import requests
import json

def list_event_types(req):
  context = {
    "event_type_list": EventType.objects.all()
  }
  return render(req, "pmucon/unicorn/event_type_list.html", context)

def show_event_type(req, et_id):
  et = get_object_or_404(EventType, pk=et_id)
  context = {
    "event_type": et,
    "xml": et.to_xml(),
    "elements": et.elements.all()
  }
  return render(req, 'pmucon/unicorn/event_type.html', context)


def edit_event_type(req, et_id):
  pass


def delete_event_type(req, et_id):
  pass

