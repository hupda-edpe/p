from django import forms

class EventTypeForm(forms.Form):
  et_name = forms.CharField()

class EventTypeElementForm(forms.Form):
  el_name = forms.CharField(max_length=200)
  el_type = forms.CharField(max_length=200)
  min_occurs = forms.IntegerField()
  max_occurs = forms.IntegerField()