from django.shortcuts import render
from django.http import HttpResponse

from .forms import PostProperty


def index(request):
    return HttpResponse('hello')


def property_create(request):
    form = PostProperty()
    return render(request, 'post_property.html', {'form': form})
