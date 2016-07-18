from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from pmucon.models import *

from pmucon import unicorn_wrapper

import requests
import json

def list_event_types(req):
  if req.method == 'POST':
    et_name = req.POST.get('et_name','')
    EventType(et_name=et_name).save()
  elif req.GET.get('action','') == 'delete':
    et_id = req.GET.get('et_id', -1)
    et = get_object_or_404(EventType, pk=et_id)
    et.delete()
  elif req.GET.get('action','') == 'sync':
    et_id = req.GET.get('et_id', -1)
    et = get_object_or_404(EventType, pk=et_id)
    unicorn_wrapper.syncEventType(et)

  context = {
    "event_type_list": EventType.objects.all()
  }
  return render(req, "pmucon/unicorn/event_type_list.html", context)

def show_event_type(req, et_id):
  et = get_object_or_404(EventType, pk=et_id)
  if req.method == 'POST':
    action = req.POST.get('action', '')
    if action == 'edit_event_type':
      et_name = req.POST.get('et_name', '')
      et.et_name = et_name
      et.save()
    elif action == 'edit_event_type_element':
      el_id = req.POST.get('el_id', -1)
      el = get_object_or_404(EventTypeElement, pk=el_id)
      el.el_name = req.POST.get('el_name', '')
      el.el_type = req.POST.get('el_type', '')
      el.min_occurs = req.POST.get('min_occurs', '')
      el.max_occurs = req.POST.get('max_occurs', '')
      el.save()
    elif action == 'new_event_type_element':
      el = EventTypeElement(
        event_type=et,
        el_name = req.POST.get('el_name', ''),
        el_type = req.POST.get('el_type', ''),
        min_occurs = req.POST.get('min_occurs', ''),
        max_occurs = req.POST.get('max_occurs', ''),
      )
      el.save()
  elif req.GET.get('action','') == 'delete':
    el_id = req.GET.get('el_id', -1)
    el = get_object_or_404(EventTypeElement, pk=el_id)
    el.delete()

  context = {
    "event_type": et,
    "xml": et.to_xml(),
    "elements": et.elements.all()
  }
  return render(req, 'pmucon/unicorn/event_type.html', context)

def edit_event_type(req, et_id):
  event_type = get_object_or_404(EventType, pk=et_id)
  return render(req, 'pmucon/unicorn/edit_event_type.html', {'event_type': event_type})

def new_event_type(req):
  return render(req, 'pmucon/unicorn/new_event_type.html', {})

def edit_event_type_element(req, et_id, el_id):
  event_type = get_object_or_404(EventType, pk=et_id)
  event_type_element = get_object_or_404(EventTypeElement, pk=el_id)
  context = {
    'event_type': event_type,
    'event_type_element': event_type_element,
    'action': 'edit_event_type_element'
  }
  return render(req, 'pmucon/unicorn/edit_event_type_element.html', context)

def new_event_type_element(req, et_id):
  event_type = get_object_or_404(EventType, pk=et_id)
  event_type_element = EventTypeElement(event_type=event_type)
  context = {
    'event_type': event_type,
    'event_type_element': event_type_element,
    'action': 'new_event_type_element'
  }
  return render(req, 'pmucon/unicorn/edit_event_type_element.html', context)

