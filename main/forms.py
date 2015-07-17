from django import forms
from django.core.validators import RegexValidator
from main.models import City

class CitySearchForm(forms.Form):
    alphanumeric = RegexValidator(r'^[a-zA-Z\s]*$', "Please Type Letters")
    name = forms.CharField(required=True, 
                                initial="Orem",
                                validators=[alphanumeric],
                                widget=forms.TextInput(attrs={'class': "form-control"}
                                ))

    state = forms.CharField(required=True, initial="Utah", 
                                validators=[alphanumeric],
                                widget=forms.TextInput(attrs={'class': "form-control"}
                                ))


class CreateCityForm(forms.ModelForm):
    class Meta:
        model = City