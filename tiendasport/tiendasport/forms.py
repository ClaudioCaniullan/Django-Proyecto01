from django import forms

class RegistroForm(forms.Form):
    username = forms.CharField(required=True,
                               min_length=4,
                               max_length=50)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)