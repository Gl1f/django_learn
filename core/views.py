from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {
        "name": "Максим",
        "title": "BarberShop",
    }
    return render(request, "core/index.html", context)