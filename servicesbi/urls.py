from django.urls import path
from . import views

app_name = "servicesbi"

urlpatterns = [
    # HOME
    path("", views.home, name="home"),

    # PÁGINAS
    path("python/", views.python, name="python"),
    path("power-bi/", views.powerbi, name="powerbi"),
    path("automacoes/", views.automacoes, name="automacoes"),
    path("excel/", views.excel, name="excel"),
    path("curriculo/", views.curriculo, name="curriculo"),
    path("contato/", views.contato, name="contato"),
]
