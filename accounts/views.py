from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm

# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registerUser')

        
    form = UserForm()
    context = {
        'form' : form,
    }
    return render (request, 'accounts/registerUser.html', context)
