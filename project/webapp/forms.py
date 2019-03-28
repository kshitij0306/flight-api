from django import forms

class FlightForm(forms.Form):
    flight_no=forms.CharField(label='flight number',max_length=6)
