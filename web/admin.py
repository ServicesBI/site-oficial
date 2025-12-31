from django.contrib import admin
from .models import Curriculo


@admin.register(Curriculo)
class CurriculoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "updated_at")
