import requests, json
#from pmucon import unicorn_config
URL = "http://172.18.0.3:8080/Unicorn/webapi/REST/"

def postEventType():
  xml = """<?xml version="1.0" encoding="utf-8"?>
    <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns="ProcessmakerEvent.xsd" targetNamespace="ProcessmakerEvent.xsd" elementFormDefault="qualified">
      <xs:element name="ProcessmakerEvent">
        <xs:complexType>
          <xs:sequence>
          <xs:element name="AppUid" type="xs:string" minOccurs="1" maxOccurs="1" />
          <xs:element name="Timestamp" type="xs:dateTime" minOccurs="1" maxOccurs="1" />
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:schema>
  """

  payload = {
    "xsd": xml,
    "schemaName": "ProcessmakerEvent",
    "timestampName": "Timestamp"
  }

  return requests.post(URL + "EventType", headers={"content-type": "application/json"}, data=json.dumps(payload))

def postEvent(app_uid):

  event = """<?xml version="1.0" encoding="UTF-8" standalone="no"?> 
    <cpoi xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="ProcessmakerEvent.xsd"> 
      <AppUid>{appuid}</AppUid> 
      <Timestamp>2015-09-05T20:05:32.799</Timestamp> 
    </cpoi>
  """.format(appuid=app_uid)

  return requests.post(URL + "Event", data=event)

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

  return requests.post(URL + "EventQuery/REST", headers={"content-type": "application/json"}, data=json.dumps(payload))

def parseQueryMatch(qm):
  pass