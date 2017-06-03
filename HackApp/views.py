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
        house.score = math.sqrt((house.lat - decimal.Decimal(lat))**2 + (house.lon - decimal.Decimal(lon))**2)

        # Modify score by services available
        services = AvailableService.objects.filter(house=house)
        for service in services:
            house.score -= service.weight

    # Sort based on location
    houses = list(houses)
    houses.sort(key=lambda house: house.score)
    return house

# Create your views here.
def basic(request):
    return render(request, "HackApp/index.html")
