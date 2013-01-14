from django import forms

class AddBuildingForm(forms.Form):
    building_name = forms.CharField()
    short_name = forms.CharField()
    date_added = forms.DateTimeField()
