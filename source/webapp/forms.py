from django import forms
from django.forms import widgets
from webapp.models import *


class TrackerForm(forms.Form):
    summary = forms.CharField(max_length=100, required=True, label='summary')
    description = forms.CharField(max_length=25000, required=False, label='description', widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False, label='status', empty_label=None)
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=False, label='type', empty_label=None)


class StatusForm(forms.Form):
    status = forms.CharField(max_length=30, required=True, label=type)


class TypeForm(forms.Form):
    type = forms.CharField(max_length=30, required=True, label=type)