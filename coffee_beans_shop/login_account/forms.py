from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField( max_length=20, required=True)
    last_name = forms.CharField( max_length=20, required=True)
    email = forms.EmailField(required=True)
    
    