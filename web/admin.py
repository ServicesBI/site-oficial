from django.contrib import admin
from django import forms

from .models import (
    Page,
    ServiceCard,
    ProjectCard,
    ContactContent,
)

# ======================================================
# INLINES
# ======================================================
class ServiceCardInline(admin.TabularInline):
    model = ServiceCard
    extra = 0
    ordering = ("ordem",)
    prepopulated_fields = {"slug": ("titulo",)}


class ProjectCardInline(admin.TabularInline):
    model = ProjectCard
    extra = 0
    ordering = ("ordem",)
    prepopulated_fields = {"slug": ("titulo",)}


# ======================================================
# ADMIN BASE PAGE
# ======================================================
class PageAdmin(admin.ModelAdmin):
    list_display = ("get_page_name",)
    list_filter = ()
    search_fields = ("titulo",)

    inlines = [ServiceCardInline, ProjectCardInline]

    fieldsets = (
        ("Conteúdo", {
            "fields": ("titulo", "subtitulo", "texto")
        }),
        ("Banner", {
            "fields": ("banner_image",)
        }),
        ("Currículo (apenas para a página Currículo)", {
            "fields": (
                "curriculo_folha_1",
                "curriculo_folha_2",
                "curriculo_pdf",
            )
        }),
    )

    def get_page_name(self, obj):
        return obj.get_slug_display()

    get_page_name.short_description = "Página"

    def has_add_permission(self, request):
        return False


# ======================================================
# REGISTRO PAGE
# ======================================================
@admin.register(Page)
class PageAdminRegistered(PageAdmin):
    pass


# ======================================================
# CONTATO (SEPARADO)
# ======================================================
@admin.register(ContactContent)
class ContactContentAdmin(admin.ModelAdmin):
    list_display = ("email", "telefone", "updated_at")
