from django import forms
from django.contrib.auth.models import User,auth
from .models import Depense,Budget




class Expenseform(forms.ModelForm):
    class Meta:
        model = Depense
        fields = ('categorie','categorie','montant','description')
class Budform(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ('budgets',)
