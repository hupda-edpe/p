from django.shortcuts import render, get_object_or_404

from pmucon.models import *
from pmucon import pm_wrapper, unicorn_wrapper


def list_cases(req):
  if req.GET.get('action','') == 'push':
    if req.GET.get('case', '') == 'all':
      cases = Case.objects.filter(status='new')
      for case in cases:
        push_case(case)
    else:
      case = get_object_or_404(Case, pk=req.GET.get('case', ''))
      push_case(case)
  elif req.GET.get('action','') == 'route':
      case = get_object_or_404(Case, pk=req.GET.get('case', ''))
      pm_wrapper.PMWrapper().routeCase(case.app_uid)
      case.status = 'routed'
      case.save()

  pm_wrapper.PMWrapper().pullIntermediate()

  cases = Case.objects.all()
  context = {
    'cases': cases
  }
  return render(req, 'pmucon/processmaker/list_cases.html', context)

def push_case(case):
  ev = Event(schema=case.event, app_uid=case.app_uid)
  
  if not case.waiting:
    pm_wrapper.PMWrapper().routeCase(case.app_uid)
    case.status = 'routed'
  elif case.status == 'new':
    case.status = 'pushed'
  
  case.save()
  unicorn_wrapper.postEvent(ev)
