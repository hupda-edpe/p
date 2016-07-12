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

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pmauth/', views.pmAuth, name='pmauth'),
    url(r'^startcases/', views.listStartCases, name='startcases'),
    url(r'^pullcases/', views.pullCases, name='pullcases'),
    url(r'^postevent/(?P<app_uid>[0-9a-zA-Z]+)/', views.postEvent, name='postevent'),
    url(r'^catch/', views.catchMatch, name='catch'),
    url(r'^routecase/(?P<app_uid>[0-9a-zA-Z]+)/', views.routeCase, name='routecase'),
    url(r'^deletecases/', views.deleteCases, name='deletecases')
]