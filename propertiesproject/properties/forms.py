from django import forms

from .models import Property


class PostProperty(forms.ModelForm):

    class Meta:
        model = Property
        fields = ('location', 'price', 'num_bedrooms', )
    # location = ''
    # price = ''
    # num_bedrooms = ''
    # property_type = ''
    # added_date = ''
    # added_by = ''
    # shared_ownership_scheme = ''
    # new_development = ''
    # size_sq_ft = ''
    # size_sq_m = ''