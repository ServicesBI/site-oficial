from django.contrib import admin
from .models import Page, ServiceCard, ProjectCard, ContactContent


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("slug", "updated_at")
    readonly_fields = ("slug",)

    def has_add_permission(self, request):
        # 🔥 BLOQUEIA criar páginas se já existirem
        return not Page.objects.exists()


@admin.register(ServiceCard)
class ServiceCardAdmin(admin.ModelAdmin):
    list_display = ("titulo", "page", "ordem")
    list_filter = ("page",)
    ordering = ("ordem",)


@admin.register(ProjectCard)
class ProjectCardAdmin(admin.ModelAdmin):
    list_display = ("titulo", "page", "ativo", "ordem")
    list_filter = ("page",)
    ordering = ("ordem",)


@admin.register(ContactContent)
class ContactContentAdmin(admin.ModelAdmin):
    list_display = ("page", "email", "telefone")
