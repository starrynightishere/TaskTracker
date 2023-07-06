from dataclasses import fields
from django import forms

from . models import data, analysis
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DataForm(forms.ModelForm):

    # required_css_class = 'required-field'
    # which_day = forms.CharField(widget=forms.TextInput(attrs={"class":"control", "placeholder":"Which day"}))
    # tasks = forms.CharField(widget=forms.TextInput(attrs={"class":"control", "placeholder":"Tasks performed"}))
    # happiness_score = forms.CharField(widget=forms.TextInput(attrs={"class":"control", "placeholder":"Happiness Score"}))

    required_css_class = 'required-field'
    which_day = forms.CharField(widget=forms.TextInput(attrs={"class":"cinputbox", "placeholder":"Which day"}))
    tasks = forms.CharField(widget=forms.TextInput(attrs={"class":"cinputbox", "placeholder":"Tasks performed"}))
    happiness_score = forms.CharField(widget=forms.TextInput(attrs={"class":"cinputbox", "placeholder":"Happiness Score"}))

    class Meta:
        model = data
        fields = '__all__'
        # widgets = {
        #     # 'which_day': forms.TextInput(attrs={'class': 'form-control', 'style':'width:300px;','placeholder':'Which day is it?'}),
        #     'which_day': forms.TextInput(attrs={'class':'form-control'}),
        #     # 'tasks': forms.TextInput(attrs={'class': 'form-control', 'style':'width:300px;', 'placeholder':'Tasks performed'}),
        #     'tasks': forms.TextInput(attrs={'class':'form-control'}),

        #     # 'happiness_score': forms.TextInput(attrs={'class': 'form-control', 'style':'width:300px;', 'placeholder':'Happiness score of the day'}
        #     'happiness_score': forms.TextInput(attrs={'class':'form-control'})
            


        # }




class analysisform(forms.ModelForm):

    # day_of_analysis = forms.CharField(widget=forms.TextInput(attrs={"class":"analysis-control", "placeholder":"Which "}))

    class Meta:
        model = analysis
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']