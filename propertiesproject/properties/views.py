import logging

from django.shortcuts import render
from django.http import HttpResponse

from .forms import PostProperty, QueryProperty
from .models import Property

log = logging.getLogger(__name__)


def index(request):
    if request.method == 'POST':
        form = QueryProperty(request.POST)
        if form.is_valid():
            form_values = form.cleaned_data
            # Obviously this is not going to work, so factor
            # out a function to prepare queries depending
            # on what parameters are present and what do they say
            # watchful with property type "Any".
            properties = Property.objects.filter(
                price__gte=form_values['min_price'],
                price__lte=form_values['max_price'],
                property_type=form_values['property_type'],
                num_bedrooms=form_values['bedrooms'],
            )
            log.debug(properties)
            return render(request, 'home.html', {'form': form, 'properties': properties})
    else:
        form = QueryProperty()
    return render(request, 'home.html', {'form': form})


def property_add(request):
    if request.method == 'POST':
        form = PostProperty(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('thanks!')
    else:
        form = PostProperty()
    return render(request, 'post_property.html', {'form': form})


def property_create(request):
    log.debug('Receiving request...')
    form = PostProperty()
    return render(request, 'post_property.html', {'form': form})
