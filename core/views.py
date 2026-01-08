from django.shortcuts import render
from dataclasses import dataclass
from django.http import Http404


@dataclass
class Name:
    name: str
    age: int

    @property
    def age_in_days(self) -> int:
        return self.age * 365

MASTERS = [
    {"id": 1, "name": "Андрей", "level": "middle"},
    {"id": 2, "name": "Олег", "level": "senior"},
    {"id": 3, "name": "Ирина", "level": "junior"},
]

def index(request):
    context = {
        'title': 'Главная',
        "name": "Арбуз",
        "integer": 1,
        "float": 1.0,
        "string": "строка",
        "num_list": [1, 2, 3],
        "name_dict": {"name": "Арбуз", "price": 100},
        "string_set": {"red", "green", "yellow"},
        "name_object": Name("Алевтина", 25),
    }
    return render(request, "core/index.html", context)



def master_list(request):
    return render(request, "core/master_list.html", {"masters": MASTERS})

def master_detail(request, master_id: int):
    master = next((m for m in MASTERS if m["id"] == master_id), None)
    if master is None:
        raise Http404("Master not found")
    return render(request, "core/master_detail.html", {"master": master})