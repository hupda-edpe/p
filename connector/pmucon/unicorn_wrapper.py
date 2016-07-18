from pmucon.config import unicorn_config

import requests, json

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


def postEvent(ev):
  xml = ev.to_xml()
  return requests.post(unicorn_config.URL + "Event", data=xml)



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