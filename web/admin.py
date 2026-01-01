from django.contrib import admin
from django import forms

from .models import (
    Page,
    PageTheme,
    ServiceCard,
    ProjectCard,
    Curriculo,
    ContactContent,
)


# ======================================================
# WIDGET CUSTOMIZADO: HEX + CAIXINHA DE COR
# ======================================================
class ColorHexWidget(forms.Widget):
    template_name = "admin/widgets/color_hex.html"

    def value_from_datadict(self, data, files, name):
        return data.get(name)


# ======================================================
# FORM DO TEMA DA PÁGINA
# ======================================================
class PageThemeAdminForm(forms.ModelForm):
    class Meta:
        model = PageTheme
        fields = "__all__"
        widgets = {
            "menu_color": ColorHexWidget(),
            "title_color": ColorHexWidget(),
            "subtitle_color": ColorHexWidget(),
            "text_color": ColorHexWidget(),

            "services_title_color": ColorHexWidget(),
            "services_text_color": ColorHexWidget(),
            "services_border_color": ColorHexWidget(),
            "services_button_color": ColorHexWidget(),

            "projects_title_color": ColorHexWidget(),
            "projects_text_color": ColorHexWidget(),
            "projects_border_color": ColorHexWidget(),
            "projects_button_color": ColorHexWidget(),
        }


# ======================================================
# ADMIN — PÁGINAS
# ======================================================
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("slug", "titulo", "updated_at")
    list_filter = ("slug",)
    search_fields = ("titulo",)

    fieldsets = (
        ("Identificação da Página", {
            "fields": ("slug",)
        }),
        ("Conteúdo", {
            "fields": ("titulo", "subtitulo", "texto")
        }),
        ("Banner", {
            "fields": ("banner_image",)
        }),
    )


# ======================================================
# ADMIN — TEMA DA PÁGINA
# ======================================================
@admin.register(PageTheme)
class PageThemeAdmin(admin.ModelAdmin):
    form = PageThemeAdminForm
    list_display = ("page", "updated_at")

    fieldsets = (
        ("Página", {
            "fields": ("page",)
        }),

        ("Menu", {
            "fields": ("menu_color",)
        }),

        ("Hero / Texto", {
            "fields": (
                "title_color",
                "subtitle_color",
                "text_color",
            )
        }),

        ("Serviços", {
            "fields": (
                "services_title_color",
                "services_text_color",
                "services_border_color",
                "services_button_color",
            )
        }),

        ("Projetos", {
            "fields": (
                "projects_title_color",
                "projects_text_color",
                "projects_border_color",
                "projects_button_color",
            )
        }),
    )

    class Media:
        js = ("admin/js/color_sync.js",)


# ======================================================
# ADMIN — SERVIÇOS (CARDS)
# ======================================================
@admin.register(ServiceCard)
class ServiceCardAdmin(admin.ModelAdmin):
    list_display = ("titulo", "page", "ordem")
    list_filter = ("page",)
    list_editable = ("ordem",)
    search_fields = ("titulo",)
    prepopulated_fields = {"slug": ("titulo",)}


# ======================================================
# ADMIN — PROJETOS (CARDS)
# ======================================================
@admin.register(ProjectCard)
class ProjectCardAdmin(admin.ModelAdmin):
    list_display = ("titulo", "page", "ativo", "ordem")
    list_filter = ("page", "ativo")
    list_editable = ("ativo", "ordem")
    search_fields = ("titulo",)
    prepopulated_fields = {"slug": ("titulo",)}


# ======================================================
# ADMIN — CURRÍCULO
# ======================================================
@admin.register(Curriculo)
class CurriculoAdmin(admin.ModelAdmin):
    list_display = ("page", "updated_at")


# ======================================================
# ADMIN — CONTATO
# ======================================================
@admin.register(ContactContent)
class ContactContentAdmin(admin.ModelAdmin):
    list_display = ("page", "email", "telefone", "updated_at")
