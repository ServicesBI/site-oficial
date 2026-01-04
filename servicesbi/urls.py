from django.urls import path
from . import views

app_name = "servicesbi"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("python/", views.python, name="python"),
    path("power-bi/", views.powerbi, name="powerbi"),
    path("automacoes/", views.automacoes, name="automacoes"),
    path("excel/", views.excel, name="excel"),
    path("curriculo/", views.curriculo, name="curriculo"),
    path("contato/", views.contato, name="contato"),
]
