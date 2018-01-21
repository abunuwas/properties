from django import forms

from .models import Property, PROPERTY_TYPES


ANY = 'ANY'

PROPERTY_TYPES.append((ANY, 'Any'))

class QueryProperty(forms.Form):
    location = forms.CharField(max_length=200)
    min_price = forms.IntegerField()
    max_price = forms.IntegerField()
    property_type = forms.ChoiceField(
        choices=PROPERTY_TYPES,
    )
    bedrooms = forms.IntegerField()


class PostProperty(forms.ModelForm):

    class Meta:
        model = Property
        fields = (
            'city',
            'country',
            'postal_code',
            'price',
            'num_bedrooms',
            'property_type',
            'shared_ownership_scheme',
            'new_development',
            'size_sq_ft',
            'size_sq_m',
        )
