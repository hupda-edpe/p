from django.shortcuts import render, get_object_or_404

from pmucon.models import *
from pmucon import pm_wrapper

def inbox(req):
  #auth = pm_auth.get_auth_hdr()
  pass


def list_cases(req):
  if req.GET.get('action','') == 'pull':
    # pull
    pass

  cases = Case.objects.all()

  context = {
    'cases': cases
  }

  return render(req, 'pmucon/processmaker/list_cases.html', context)



  # process
  #   retrieve variables
  #   make event
  #   send to unicorn
  #   route immediatly if desired