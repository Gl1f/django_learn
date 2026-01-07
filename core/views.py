from django.shortcuts import render
from dataclasses import dataclass


@dataclass
class Name:
    name: str
    age: int

    @property
    def age_in_days(self) -> int:
        return self.age * 365


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