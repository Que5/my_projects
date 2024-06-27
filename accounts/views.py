from django.shortcuts import render
from .forms import UserForm

# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        print()
    form = UserForm()
    context = {
        'form' : form,
    }
    return render (request, 'accounts/registerUser.html', context)
