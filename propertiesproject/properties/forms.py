from django import forms

from .models import Property


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
