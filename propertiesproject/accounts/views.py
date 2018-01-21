from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('you are in accounts index view.')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('You signed up!')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
