"""pmucon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views, unicorn_views, pm_views

urlpatterns = [
  url(r'^$', views.index, name='index'),

  url(r'^cases/?$',                            pm_views.list_cases,  name='cases'),
  url(r'^cases/push/?$',                       pm_views.push_all,    name='push_all'),
  url(r'^cases/(?P<case_id>[0-9]+)/push/?$',   pm_views.push_case,   name='push_case'),
  url(r'^cases/(?P<case_id>[0-9]+)/route/?$',  pm_views.route_case,  name='route_case'),
  url(r'^cases/(?P<case_id>[0-9]+)/delete/?$', pm_views.delete_case, name='delete_case'),



  url(r'^event_type/?$',                          unicorn_views.list_event_types, name='list_event_types'),
  url(r'^event_type/(?P<et_id>[0-9]+)/?$',        unicorn_views.show_event_type,  name='show_event_type'),
  url(r'^event_type/(?P<et_id>[0-9]+)/edit/?$',   unicorn_views.edit_event_type,  name='edit_event_type'),
  url(r'^event_type/new/?$',                      unicorn_views.new_event_type,   name='new_event_type'),

  url(r'^event_type/(?P<et_id>[0-9]+)/new/?$',    unicorn_views.new_event_type_element,
                                                                                  name='new_event_type_element'),
  url(r'^event_type/(?P<et_id>[0-9]+)/(?P<el_id>[0-9]+)/edit/?$',
                                                  unicorn_views.edit_event_type_element,
                                                                                  name='edit_event_type_element'),

  url(r'^event_query/?$',                             unicorn_views.list_event_queries, name='list_event_queries'),
  url(r'^event_query/new/?$',    unicorn_views.new_event_query,    name='new_event_query'),
  url(r'^event_query/(?P<query_id>[0-9]+)/edit/?$',   unicorn_views.edit_event_query,   name='edit_event_query'),
  url(r'^event_query/(?P<query_id>[0-9]+)/delete/?$', unicorn_views.delete_event_query, name='delete_event_query'),
  url(r'^event_query/(?P<query_id>[0-9]+)/sync/?$',   unicorn_views.sync_event_query,   name='sync_event_query'),
]



"""
  url(r'^startcases/?$',                          views.listStartCases, name='startcases'),
  url(r'^pullcases/?$',                           views.pullCases,      name='pullcases'),
  url(r'^postevent/(?P<app_uid>[0-9a-zA-Z]+)/?$', views.postEvent,      name='postevent'),
  url(r'^catch/?$',                               views.catchMatch,     name='catch'),
  url(r'^routecase/(?P<app_uid>[0-9a-zA-Z]+)/?$', views.routeCase,      name='routecase'),
  url(r'^deletecases/?$',                         views.deleteCases,    name='deletecases'),
"""