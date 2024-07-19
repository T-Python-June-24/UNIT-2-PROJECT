from django import forms

class AddToItineraryForm(forms.Form):
        activity_id = forms.IntegerField(widget=forms.HiddenInput)
