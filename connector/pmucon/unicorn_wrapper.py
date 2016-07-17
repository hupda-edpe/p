from pmucon.config import unicorn_config

import requests, json


############### EVENT TYPES ##################

def syncEventType(event_type):
  if not event_type.to_xml() == getEventType(event_type):
    deleteEventType(event_type)
    postEventType(event_type).raise_for_status()

def postEventType(event_type):
  payload = {
    "xsd": event_type.to_xml(),
    "schemaName": event_type.et_name,
    "timestampName": "Timestamp"
  }
  return requests.post(unicorn_config.URL + "EventType", headers={"content-type": "application/json"}, data=json.dumps(payload))

def getEventType(event_type):
  name = event_type.et_name
  resp = requests.get(unicorn_config.URL + "EventType/" + name)
  if resp.status_code == 200:
    return resp.text
  else:
    return None

def deleteEventType(event_type):
  name = event_type.et_name
  resp = requests.delete(unicorn_config.URL + "EventType/" + name)


################ EVENTS #######################



def postEvent(app_uid):

  event = """<?xml version="1.0" encoding="UTF-8" standalone="no"?> 
    <cpoi xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="ProcessmakerEvent.xsd"> 
      <AppUid>{appuid}</AppUid> 
      <Timestamp>2015-09-05T20:05:32.799</Timestamp> 
    </cpoi>
  """.format(appuid=app_uid)

  return requests.post(unicorn_config.URL + "Event", data=event)

def postQuery():
  queryString = "SELECT * FROM ProcessmakerEvent"
  title = "PMQuery"
  email = "test@test.de"
  notificationPath = "http://141.20.192.110:8000/catch/"

  payload = {
    "queryString": queryString,
    "title": title,
    "email": email,
    "notificationPath": notificationPath
  }

  return requests.post(unicorn_config.URL + "EventQuery/REST", headers={"content-type": "application/json"}, data=json.dumps(payload))

def parseQueryMatch(qm):
  pass