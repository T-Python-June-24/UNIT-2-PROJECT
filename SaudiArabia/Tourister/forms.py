# forms.py
from django import forms

class DataForm(forms.Form):
    field_name = forms.CharField(label='Field Name', max_length=100)
    field_value = forms.CharField(label='Field Value', max_length=100)
