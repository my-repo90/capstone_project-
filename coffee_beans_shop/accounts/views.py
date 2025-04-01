from django.shortcuts import render , redirect
from .forms import CreationForms
# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = CreationForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
        
        else:
            form = CreationForms()
        return render(request , 'registration/register.html' , {'form' : form}) 

