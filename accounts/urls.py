from django.urls import path ,include
from .views import Home
from . import views

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("Equipments/",views.Equipments,name="Equipments"),
    path("Measurements/",views.test, name="test"),
    # path("Basics/",views.Basics,name = "Basics"),
    # path("basic/Basics/",views.Basics,name = "Basics"),
    #path("test/",views.test,name="test"),

    ]