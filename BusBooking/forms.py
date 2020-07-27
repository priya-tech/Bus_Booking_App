from django import forms
from django.forms import ModelForm
from .models import AdduserModel,AddRouteModel,AddBusModel

class AdduserForm(ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)
    Gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'class': 'bootstrap-select'}), choices=(('male','Male'),('female','Female'),))
    class Meta:
        model=AdduserModel
        fields=['Name','Email','Password','Gender','Age','Phone']

class AddRouteForm(ModelForm):
    class Meta:
        model=AddRouteModel
        fields=['Route_id','Bus_from','Bus_to','Journey_time','Price_per_seat']

class AddBusForm(ModelForm):
    class Meta:
        model=AddBusModel
        fields=['Bus_number','Route','Start_time','Total_seats']
