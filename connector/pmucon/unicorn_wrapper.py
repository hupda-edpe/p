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


def syncEventQuery(query):
  if not query.query_string == getEventQuery(query):
    deleteEventQuery(query)
    postEventQuery(query)


def postEventQuery(query):
  payload = {
    "queryString": query.query_string,
    "title": query.title,
    "email": query.email,
    "notificationPath": unicorn_config.CALLBACK
  }
  r = requests.post(unicorn_config.URL + "EventQuery/REST", headers={"content-type": "application/json"}, data=json.dumps(payload))
  r.raise_for_status()
  query.uuid = r.text
  query.save()

def getEventQuery(query):
  return requests.get(unicorn_config.URL + "EventQuery/" + query.uuid).text

def deleteEventQuery(query):
  return requests.delete(unicorn_config.URL + "EventQuery/REST/" + query.uuid)
