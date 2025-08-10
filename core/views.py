from django.shortcuts import render
from django.http import HttpResponse

MASTERS = [
    {"id": 1, "name": "Алевтина", "skill": "Fade"},
    {"id": 2, "name": "Борис", "skill": "Classic"},
]

# Create your views here.
def index(request):
    context = {'name': 'Арбуз'}
    return render(request, 'first_template.html', context)

def masters_list(request):
    context = {'masters': MASTERS}
    return render(request, 'masters/list.html', context)

def master_detail(request, name: str):
    # нормализуем регистр и "обрезаем" пробелы по краям
    key = name.strip().lower()
    master = next((m for m in MASTERS if m["name"].strip().lower() == key), None)
    return render(request, "masters/detail.html", {"master": master, "name": name})
