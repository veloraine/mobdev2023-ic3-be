from django.urls import path
from .views import *

app_name = "pokemon"

urlpatterns = [
    path("list", pokemon_list, name="pokemon_list"),
    path("create", pokemon_create, name="pokemon_create"),
]
