from django.shortcuts import render
from django.http import HttpResponse

class Name:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} лет"
    
    def age_in_days(self):
        return self.age * 365

# Create your views here.
def index(request):
    context = {
        "name": "Арбуз",
        "integer": 1,
        "float": 1.0,
        "string": "строка",
        "num_list": [1, 2, 3],
        "name_dict": {"name": "Арбуз", "price": 100},
        "string_set": {"red", "green", "yellow"},
        "name_object": Name("Алевтина", 25),
    }
    return render(request, "first_template.html", context)