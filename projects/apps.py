from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projects'

list_display = ('title', 'page', 'is_active', 'order')
list_filter = ('page', 'is_active')

