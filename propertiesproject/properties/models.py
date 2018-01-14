from django.db import models


class Location(models.Model):
    pass


class PropertyType(models.Model):
    pass


class SharedOwnershipScheme(models.Model):
    pass


class Property(models.Model):
    location = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    num_bedrooms = models.CharField(max_length=50)
    property_type = models.CharField(max_length=50)
    added_date = models.CharField(max_length=50)
    added_by = models.CharField(max_length=50)
    shared_ownership_scheme = models.CharField(max_length=50)
    new_development = models.CharField(max_length=50)
    size_sq_ft = models.CharField(max_length=50)
    size_sq_m = models.CharField(max_length=50)
