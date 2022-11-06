from django import forms

class MotoFormulario(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    edad = forms.IntegerField()