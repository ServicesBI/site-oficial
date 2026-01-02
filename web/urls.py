from django.contrib import admin
from django.urls import path
from web.views import (
    home,
    curriculo_view,
    contato_view,
    page_by_slug,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),
    path("curriculo/", curriculo_view, name="curriculo"),
    path("contato/", contato_view, name="contato"),

    path("<slug:slug>/", page_by_slug, name="page"),
]
