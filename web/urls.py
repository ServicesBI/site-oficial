from django.urls import path
from web.views import page_by_slug

urlpatterns = [
    path("", page_by_slug, name="home"),
    path("<slug:slug>/", page_by_slug, name="page"),
]

