from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("masters/", views.master_list, name="master_list"),
    path("masters/<int:master_id>/", views.master_detail, name="master_detail"),
]
