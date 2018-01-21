import logging

from django.shortcuts import render
from django.http import HttpResponse

from .forms import PostProperty
from .models import Property

log = logging.getLogger(__name__)


def index(request):
    return HttpResponse('hello')


def property_add(request):
    log.info('Receiving request...')
    if request.method == 'POST':
        form = PostProperty(request.POST)
        if form.is_valid():
            log.debug(form.cleaned_data)
            property = Property.objects.create(**form.cleaned_data)
            property.save()
            return HttpResponse('thanks!')
    else:
        form = PostProperty()
    return render(request, 'post_property.html', {'form': form})


def property_create(request):
    log.debug('Receiving request...')
    form = PostProperty()
    return render(request, 'post_property.html', {'form': form})
