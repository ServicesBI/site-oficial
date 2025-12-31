from django.contrib import admin
from .models import Curriculo, SiteTheme


@admin.register(Curriculo)
class CurriculoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "updated_at")


@admin.register(SiteTheme)
class SiteThemeAdmin(admin.ModelAdmin):
    list_display = ("nome", "updated_at")
