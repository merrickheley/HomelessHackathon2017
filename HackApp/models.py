from django.db import models

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

HOUSE = "H"
APART = "A"
ACCOMM_TYPE = (
    (HOUSE, 'House'),
    (APART, 'Apartment'),
)

class House(models.Model):

    address = models.CharField(max_length=200)
    post_code = models.CharField(max_length=6)
    photo = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=30)
    contact_phone = models.CharField(max_length=15)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    pets = models.BooleanField(default=True)
    accommodation_length = models.CharField(
        max_length=2,
        choices=ACCOMM_CHOICES,
        default=SHORTTERM,
    )
    tenant_type = models.CharField(
        max_length=2,
        choices=TENANT_CHOICES,
        default=HOMELESS,
    )
    accommodation_type = models.CharField(
        max_length=2,
        choices=ACCOMM_TYPE,
        default=HOUSE,
    )
    def __str__(self):
        return self.address + " " + self.post_code

class ServiceCategory(models.Model):
    category = models.CharField(max_length=50)
    serv_type = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return " - ".join([self.category,self.serv_type, str(self.weight)])

    class Meta:
        unique_together=("category", "serv_type")

class ServiceProvider(models.Model):
    suburb = models.CharField(max_length=200)
    post_code = models.CharField(max_length=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=200, default="", blank=True, null=True)

    def __str__(self):
        return str(self.id) + ". " + self.name

class Service(models.Model):
    category = models.ForeignKey('ServiceCategory')
    provider = models.ForeignKey('ServiceProvider')

    class Meta:
        unique_together=("category", "provider")
    def __str__(self):
        return " - ".join([str(self.category), str(self.provider)])


class AvailableProvider(models.Model):
    house = models.ForeignKey('House')
    provider = models.ForeignKey('ServiceProvider')

    def __str__(self):
        return str(self.house) + "  -  " + str(self.provider)

