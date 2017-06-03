from django.db import models

class House(models.Model):
    SHORTTERM = "ST"
    LONGTERM = "LT"
    ACCOMM_CHOICES = (
        (SHORTTERM, 'Short Term'),
        (LONGTERM, 'Long Term'),
    )

    HOMELESS = "HL"
    ATRISK = "AR"
    YOUTH = "YT"
    TENANT_CHOICES = (
        (HOMELESS, 'Homeless'),
        (ATRISK, 'At Risk'),
        (YOUTH, 'Youth'),
    )

    address = models.CharField(max_length=200)
    post_code = models.CharField(max_length=6)
    photo = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=30)
    contact_phone = models.CharField(max_length=15)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    accomodation_length = models.CharField(
        max_length=2,
        choices=ACCOMM_CHOICES,
        default=SHORTTERM,
    )
    tenant_type = models.CharField(
        max_length=2,
        choices=TENANT_CHOICES,
        default=HOMELESS,
    )

class ServiceProvider(models.Model):
    name = models.CharField(max_length=50)

class Service(models.Model):
    address = models.CharField(max_length=200)
    post_code = models.CharField(max_length=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    provider = models.ForeignKey('ServiceProvider')

class AvailableServices(models.Model):
    house = models.ForeignKey('House')
    service = models.ForeignKey('Service')

