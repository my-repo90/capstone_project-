from django import forms
from django.contrib.auth.forms import UserCreationForm

class CreationForms(UserCreationForm):
    password1 = forms.CharField(
         max_length=20, 
         required=True,
         label="password",
         widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}),
         )
    password2  = forms.CharField(
         max_length=20, 
         required=True,
         widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}),
         )
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("password1","password2")