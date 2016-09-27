"""This module contains the django-views related to ProcessMaker."""

from django.shortcuts import render, get_object_or_404

from pmucon.models import *
from pmucon import pm_wrapper, unicorn_wrapper


def list_cases(req):
  pm_wrapper.pull_cases()

  cases = Case.objects.all()
  context = {
    'cases': cases
  }
  return render(req, 'pmucon/processmaker/list_cases.html', context)

def push_all(req):
  cases = Case.objects.filter(status='new')
  for case in cases:
    push(case)
  return list_cases(req)

def push_case(req, case_id):
  case = get_object_or_404(Case, pk=case_id)
  push(case)
  return list_cases(req)

def route_case(req, case_id):
  case = get_object_or_404(Case, pk=case_id)
  pm_wrapper.route_case(case)
  case.status = 'routed'
  case.save()
  return list_cases(req)

def delete_case(req, case_id):
  case = get_object_or_404(Case, pk=case_id)
  case.delete()
  return list_cases(req)


def push(case):
  event_type = get_object_or_404(EventType, et_name=case.event_type)
  variables = pm_wrapper.get_variables(case)

  event_vars = [EventVariable(name=elem.el_name, value=variables[elem.el_name]) for elem in event_type.elements.all()]

  ev = Event(schema=case.event_type, app_uid=case.app_uid, tas_uid=case.tas_uid, pro_uid=case.pro_uid, variables=event_vars)
  
  if not (case.blocking or case.status == 'routed'):
    pm_wrapper.route_case(case)
    case.status = 'routed'
  elif case.status == 'new':
    case.status = 'pushed'
  
  case.save()
  unicorn_wrapper.postEvent(ev)