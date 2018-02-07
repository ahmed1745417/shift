from django import forms

class DateForm(forms.Form):
    startdate = forms.DateField()
    enddate = forms.DateField()
    
