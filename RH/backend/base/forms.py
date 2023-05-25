from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .models import *
from django import forms

class EmployeLogin(forms.Form):
    login = forms.CharField(label="Login",widget=forms.TextInput)
    passwd = forms.CharField(label="Password",widget=forms.PasswordInput)

    def clean(self): #on surcharge la méthode clean pour la validation des champs de formulaire
        cleaned_data=super(EmployeLogin, self).clean()
        login = cleaned_data.get('login')
        passwd = cleaned_data.get('passwd')
        if login and passwd: #si les données sont vérifiés
            employee=Employe.objects.filter(login=login,passwd=passwd)# on récupère la ligne
            if len(employee) !=1:
                raise forms.ValidationError("Utilisateur n'existe pas") #on déclenche ValidationError s'il existe un problème avec les données
        return cleaned_data #si aucune exception ValidationError n'est produite, on retourne cleaned_data

    #class Meta: #génère un formulaire depuis le modèle Employe
     #   model=Employe
     #   fields=['login','passwd'] # on définit les champs à afficher dans le form



class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = '__all__'


class CongeForm(forms.ModelForm):
    Type_choices=(
        ("Congé annuel", "Congé annuel"),
        ("Congé de maternité", "Congé de maternité"),
        ("Congé maladie", "Congé maladie"),
    )
    Type= forms.ChoiceField(choices= Type_choices)
    class Meta:
        model = Conge
        fields = '__all__'


class CompForm(forms.ModelForm):
    class Meta:
        model = Competence
        fields = '__all__'

class CompForm(forms.ModelForm):
    class Meta:
        model = Competence
        fields = '__all__'

class DiplomeForm(forms.ModelForm):
    class Meta:
        model = Diplome
        fields = '__all__'



class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = '__all__'


class FicheForm(forms.ModelForm):
    class Meta:
        model = FichePaie
        fields = '__all__'
