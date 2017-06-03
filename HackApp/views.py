from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def basic(request):
    return render(request, "HackApp/base.html")