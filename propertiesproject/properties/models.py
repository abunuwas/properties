from django.db import models


class SharedOwnershipScheme(models.Model):
    pass


class Property(models.Model):
    # Property type choices
    FLAT_APARTMENT = 'FLAT_APARTMENT'
    HOUSE = 'HOUSE'
    BUNGALOW = 'BUNGALOW'
    FARM_LAND = 'FARM_LAND'
    COMMERCIAL_PROPERTY = 'COMMERCIAL_PROPERTY'
    OTHER = 'OTHER'
    PROPERTY_TYPES = (
        (FLAT_APARTMENT, 'Flat / Apartment'),
        (HOUSE, 'House'),
        (BUNGALOW, 'Bungalow'),
        (FARM_LAND, 'Farm / Land'),
        (COMMERCIAL_PROPERTY, 'Commercial Property'),
        (OTHER, 'Other')
    )

    # Address
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)

    # Property characteristics
    price = models.FloatField()
    num_bedrooms = models.IntegerField()
    property_type = models.CharField(
        max_length=50,
        choices=PROPERTY_TYPES,
    )
    added_date = models.DateTimeField(auto_now_add=True)
    added_by = models.CharField(max_length=50)
    shared_ownership_scheme = models.CharField(max_length=50)
    new_development = models.CharField(max_length=50)
    size_sq_ft = models.FloatField()
    size_sq_m = models.FloatField()
