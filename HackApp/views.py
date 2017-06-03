import math, decimal

from django.shortcuts import render, get_object_or_404, redirect
from HackApp.models import *

def MatchHouses(lat, lon, accommodation_length=SHORTTERM, tenant_type=HOMELESS):
    # Filter based on essential criteria
    houses = House.objects.filter(accommodation_length=accommodation_length, tenant_type=tenant_type)

    # No houses, no score sort
    if len(houses) == 0:
        return []

    for house in houses:
        # Initial score is based on absolute distance
        house.score = decimal.Decimal(math.sqrt((house.lat - decimal.Decimal(lat))**2 + (house.lon - decimal.Decimal(lon))**2))

        UsedCategories = {}

        # Modify score by services available
        availableproviders = AvailableProvider.objects.filter(house=house)
        for availableprovider in availableproviders:

            services = Service.objects.filter(provider=availableprovider.provider)
            for service in services:
                if (UsedCategories.get(service.category.category) == None):
                    house.score -= service.category.weight
                    UsedCategories[service.category.category] = True

    # Sort based on location
    houses = list(houses)
    houses.sort(key=lambda house: house.score)
    return houses

# Create your views here.
def basic(request):
    return render(request, "HackApp/index.html")

def results(request):
    return render(request, "HackApp/result.html", {'houses': MatchHouses(153.0, -27.0, SHORTTERM, HOMELESS)})
