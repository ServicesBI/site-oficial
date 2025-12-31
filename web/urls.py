from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("python/", views.python, name="python"),
    path("powerbi/", views.powerbi, name="powerbi"),
    path("automacoes/", views.automacoes, name="automacoes"),
    path("excel/", views.excel, name="excel"),
    path("curriculo/", views.curriculo_view, name="curriculo"),
    path("contato/", views.contato, name="contato"),
]
