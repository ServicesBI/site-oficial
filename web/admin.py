from django.contrib import admin
from django import forms

from .models import (
    Page,
    ServiceCard,
    ProjectCard,
    ContactContent,
)

# ======================================================
# WIDGET DE COR (HEX + PICKER)
# ======================================================
class ColorHexWidget(forms.TextInput):
    template_name = "admin/widgets/color_hex.html"

    class Media:
        js = ("admin/js/color_sync.js",)


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
# PAGE ADMIN (CMS CENTRAL)
# ======================================================
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    inlines = [ServiceCardInline, ProjectCardInline]

    list_display = ("slug", "updated_at")
    search_fields = ("slug",)
    ordering = ("slug",)

    readonly_fields = ("updated_at",)

    fieldsets = (
        ("Identificação", {
            "fields": ("slug",)
        }),
        ("Hero", {
            "fields": (
                ("titulo", "titulo_color"),
                ("subtitulo", "subtitulo_color"),
                ("texto", "texto_color"),
            )
        }),
        ("Banner", {
            "fields": ("banner_image",)
        }),
        ("Menu – Cores", {
            "fields": (
                ("menu_bg_color", "menu_text_color"),
            )
        }),
        ("Serviços – Cores", {
            "fields": (
                ("services_title_color", "services_text_color"),
                ("services_border_color", "services_button_color"),
            )
        }),
        ("Projetos – Cores", {
            "fields": (
                ("projects_title_color", "projects_text_color"),
                ("projects_border_color", "projects_button_color"),
            )
        }),
        ("Footer – Cores", {
            "fields": (
                ("footer_bg_color", "footer_text_color"),
            )
       
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        color_fields = [
            "titulo_color",
            "subtitulo_color",
            "texto_color",
            "menu_bg_color",
            "menu_text_color",
            "services_title_color",
            "services_text_color",
            "services_border_color",
            "services_button_color",
            "projects_title_color",
            "projects_text_color",
            "projects_border_color",
            "projects_button_color",
            "footer_bg_color",
            "footer_text_color",
        ]

        for field in color_fields:
            if field in form.base_fields:
                form.base_fields[field].widget = ColorHexWidget()

        return form


# ======================================================
# CONTATO
# ======================================================
@admin.register(ContactContent)
class ContactContentAdmin(admin.ModelAdmin):
    list_display = ("page", "email", "updated_at")
    readonly_fields = ("updated_at",)
