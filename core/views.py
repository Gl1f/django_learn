from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': "Арбуз",
    }
    return render(request, 'first_template.html', context)