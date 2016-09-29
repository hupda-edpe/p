"""This module provides an interface for operations on Unicorn events, event
types and event queries.
"""

from pmucon.config import unicorn_config

import requests, json

def syncEventType(event_type):
  """Compare the event type xml definition between the PMU-Connector and
  Unicorn. If it differs, save the new definition to Unicorn.
  """
  if not event_type.to_xml() == getEventType(event_type):
    deleteEventType(event_type)
    postEventType(event_type).raise_for_status()

def postEventType(event_type):
  """Create new Unicorn event type."""
  payload = {
    "xsd": event_type.to_xml(),
    "schemaName": event_type.et_name,
    "timestampName": "Timestamp"
  }
  return requests.post(unicorn_config.URL + "EventType", headers={"content-type": "application/json"}, data=json.dumps(payload))

def getEventType(event_type):
  """Return the xml definition of given event type provided by Unicorn."""
  name = event_type.et_name
  resp = requests.get(unicorn_config.URL + "EventType/" + name)
  if resp.status_code == 200:
    return resp.text
  else:
    return None

def deleteEventType(event_type):
  """Delete the given event type from Unicorn"""
  name = event_type.et_name
  resp = requests.delete(unicorn_config.URL + "EventType/" + name)


def postEvent(ev):
  """Feed a new event to Unicorns event stream."""
  xml = ev.to_xml()
  return requests.post(unicorn_config.URL + "Event", data=xml)


def syncEventQuery(query):
  """Compare the event type query between the PMU-Connector and
  Unicorn. If it differs, save the new query to Unicorn.
  """
  if not query.query_string == getEventQuery(query):
    deleteEventQuery(query)
    postEventQuery(query)


def postEventQuery(query):
  """Create a new Unicorn event query"""
  payload = {
    "queryString": query.query_string,
    "title": query.title,
    "notificationPath": unicorn_config.CALLBACK
  }
  r = requests.post(unicorn_config.URL + "EventQuery/REST", headers={"content-type": "application/json"}, data=json.dumps(payload))
  r.raise_for_status()
  query.uuid = r.text
  query.save()

def getEventQuery(query):
  """Return the Unicorn event query with given UUID""" 
  return requests.get(unicorn_config.URL + "EventQuery/" + query.uuid).text

def deleteEventQuery(query):
  """Delete the Unicorn event query with given UUID"""
  return requests.delete(unicorn_config.URL + "EventQuery/REST/" + query.uuid)
