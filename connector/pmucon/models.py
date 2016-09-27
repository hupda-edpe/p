from __future__ import unicode_literals

from django.db import models

import datetime

######### UNICORN ############

class EventType(models.Model):
  et_name = models.CharField(max_length=128)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.elements = self.eventtypeelement_set

  def to_xml(self):
    xml = """<?xml version="1.0" encoding="utf-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns="{et_name}.xsd" targetNamespace="{et_name}.xsd" elementFormDefault="qualified">
  <xs:element name="{et_name}">
    <xs:complexType>
      <xs:sequence>""".format(et_name=self.et_name)

    for el in self.elements.all():
      xml += "\n        " + el.to_xml()

    xml += """
        <xs:element name="AppUid" type="xs:string" minOccurs="0" maxOccurs="1" />
        <xs:element name="ProUid" type="xs:string" minOccurs="0" maxOccurs="1" />
        <xs:element name="TasUid" type="xs:string" minOccurs="0" maxOccurs="1" />
        <xs:element name="Timestamp" type="xs:dateTime" minOccurs="1" maxOccurs="1" />
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
    """

    return xml

class EventTypeElement(models.Model):
  event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
  el_name = models.CharField(max_length=128)
  el_type = models.CharField(max_length=128, default='string')
  min_occurs = models.IntegerField(default=1)
  max_occurs = models.IntegerField(default=1)

  def to_xml(self):
    return '<xs:element name="{el_name}" type="xs:{el_type}" minOccurs="{min_occurs}" maxOccurs="{max_occurs}" />' \
      .format(el_name=self.el_name, el_type=self.el_type, min_occurs=self.min_occurs, max_occurs=self.max_occurs)


class Event():
  def __init__(self, *args, **kwargs):
    self.schema = kwargs.pop('schema', '')
    self.app_uid = kwargs.pop('app_uid', None)
    self.tas_uid = kwargs.pop('tas_uid', None)
    self.pro_uid = kwargs.pop('pro_uid', None)
    self.variables = kwargs.pop('variables', [])

  def to_xml(self):
    now = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    xml = """<?xml version="1.0" encoding="UTF-8" standalone="no"?> 
<cpoi xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="{schema}.xsd">
  <Timestamp>{timestamp}</Timestamp>""".format(schema=self.schema, timestamp=now)
    if self.app_uid:
      xml += "\n  <AppUid>{appuid}</AppUid>".format(appuid=self.app_uid)
    if self.tas_uid:
      xml += "\n  <TasUid>{tasuid}</TasUid>".format(tasuid=self.tas_uid)
    if self.pro_uid:
      xml += "\n  <ProUid>{prouid}</ProUid>".format(prouid=self.pro_uid)
    for v in self.variables:
      xml += '\n  ' + v.to_xml()
    xml += "\n</cpoi>"
    return xml


class EventVariable():
  def __init__(self, *args, **kwargs):
    self.name = kwargs.pop('name', '')
    self.value = kwargs.pop('value', '')

  def to_xml(self):
    return "<{name}>{value}</{name}>".format(name=self.name, value=self.value)



class EventQuery(models.Model):
  uuid = models.CharField(max_length=128)
  title = models.CharField(max_length=128)
  query_string = models.TextField()
  email = models.CharField(max_length=128, default='test@example.com')





##### PM STUFF ######

class Case(models.Model):
  name = models.CharField(max_length=128)
  app_uid = models.CharField(max_length=128)
  tas_uid = models.CharField(max_length=128)
  pro_uid = models.CharField(max_length=128)
  event_type = models.CharField(max_length=128)
  status = models.CharField(max_length=128)
  blocking = models.BooleanField()

class CaseVariable(models.Model):
  case = models.ForeignKey(EventType, on_delete=models.CASCADE)
  name = models.CharField(max_length=128)
  value = models.CharField(max_length=128)









#### OBSOLETE ####

class PendingEvent(models.Model):
  app_uid = models.CharField(max_length=128)
  status = models.CharField(max_length=128)

