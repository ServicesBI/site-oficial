from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_active',
        'order',
        'created_at',
    )

    list_editable = (
        'is_active',
        'order',
    )

    prepopulated_fields = {
        'slug': ('title',)
    }

    search_fields = (
        'title',
        'description',
    )

    list_filter = (
        'is_active',
        'created_at',
    )
