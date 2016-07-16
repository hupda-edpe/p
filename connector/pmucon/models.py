from __future__ import unicode_literals

from django.db import models

class PendingEvent(models.Model):
  app_uid = models.CharField(max_length=200)
  status = models.CharField(max_length=200)

class EventType(models.Model):
  et_name = models.CharField(max_length=200)

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
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
    """

    return xml

class EventTypeElement(models.Model):
  event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
  el_name = models.CharField(max_length=200)
  el_type = models.CharField(max_length=200)
  min_occurs = models.IntegerField()
  max_occurs = models.IntegerField()

  def to_xml(self):
    return '<xs:element name="{el_name}" type="xs:{el_type}" minOccurs="{min_occurs}" maxOccurs="{max_occurs}" />' \
      .format(el_name=self.el_name, el_type=self.el_type, min_occurs=self.min_occurs, max_occurs=self.max_occurs)

class EventQuery(models.Model):
  query_string = models.TextField()