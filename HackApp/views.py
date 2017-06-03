import math

from django.shortcuts import render, get_object_or_404, redirect
from HackApp.models import *

def MatchHouses(lat, long, accommodation_length=SHORTTERM, tenant_type=HOMELESS):
    # Filter based on essential criteria
    houses = House.objects.get(accommodation_length=accommodation_length, tenant_type=tenant_type)

    for house in houses:
        # Initial score is based on absolute distance
        house.score = math.sqrt((house.lat - lat)**2 + (house.long - long)**2)

        # Modify score by services available
        services = AvailableService.objects.get(house=house)
        for service in services:
            house.score -= service.weight

    # Sort based on location
    houses.sort(key=lambda house: house.score)

    return houses

# Create your views here.
def basic(request):
    return render(request, "HackApp/index.html")