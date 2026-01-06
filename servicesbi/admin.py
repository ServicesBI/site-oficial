from django.contrib import admin
from .models import (
    Page,
    ServiceCard,
    Project,
    CurriculoSection,
    ContatoText,
)

# ======================================================
# INLINES
# ======================================================

class ServiceCardInline(admin.TabularInline):
    model = ServiceCard
    extra = 0
    fields = ("title", "description", "icon", "order")
    ordering = ("order",)


class ProjectInline(admin.TabularInline):
    model = Project
    extra = 0
    fields = ("title", "description", "image", "link", "order")
    ordering = ("order",)


# ======================================================
# PAGE
# ======================================================

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("slug", "banner_title")
    list_filter = ("slug",)
    search_fields = ("banner_title",)
    ordering = ("slug",)

    fieldsets = (
        ("Identificação da Página", {
            "fields": ("slug",)
        }),
        ("Banner", {
            "fields": (
                "banner_eyebrow",
                "banner_title",
                "banner_subtitle",
                "banner_description",
            )
        }),

    )

    inlines = [
        ServiceCardInline,
        ProjectInline,
    ]


# ======================================================
# SERVICE CARD
# ======================================================

@admin.register(ServiceCard)
class ServiceCardAdmin(admin.ModelAdmin):
    list_display = ("title", "page", "order")
    list_filter = ("page",)
    ordering = ("page", "order")
    search_fields = ("title",)


# ======================================================
# PROJECT
# ======================================================

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "page", "order")
    list_filter = ("page",)
    ordering = ("page", "order")
    search_fields = ("title",)


# ======================================================
# CURRÍCULO
# ======================================================

@admin.register(CurriculoSection)
class CurriculoAdmin(admin.ModelAdmin):
    list_display = ("page",)
    fieldsets = (
        ("Currículo — Folha 1", {
            "fields": ("folha_1",)
        }),
        ("Currículo — Folha 2", {
            "fields": ("folha_2",)
        }),
    )


# ======================================================
# CONTATO
# ======================================================

@admin.register(ContatoText)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ("page",)
    fieldsets = (
        ("Textos da Página de Contato", {
            "fields": ("intro_text", "form_title")
        }),
    )
