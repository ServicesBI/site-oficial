from django.contrib import admin
from django import forms

from .models import (
    Page,
    PageTheme,
    ServiceCard,
    ProjectCard,
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
# FORM DO TEMA DA PÁGINA (INLINE)
# ======================================================
class PageThemeInlineForm(forms.ModelForm):
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
# INLINES
# ======================================================
class PageThemeInline(admin.StackedInline):
    model = PageTheme
    form = PageThemeInlineForm
    can_delete = False
    extra = 0


class ServiceCardInline(admin.TabularInline):
    model = ServiceCard
    extra = 0
    fields = ("titulo", "descricao", "imagem", "slug", "ordem")
    ordering = ("ordem",)
    prepopulated_fields = {"slug": ("titulo",)}


class ProjectCardInline(admin.TabularInline):
    model = ProjectCard
    extra = 0
    fields = ("titulo", "descricao", "imagem", "slug", "ativo", "ordem")
    ordering = ("ordem",)
    prepopulated_fields = {"slug": ("titulo",)}


# ======================================================
# ADMIN — PAGE (BASE DE TUDO)
# ======================================================
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("slug", "titulo", "updated_at")
    list_filter = ("slug",)
    search_fields = ("titulo",)

    inlines = [
        PageThemeInline,
        ServiceCardInline,
        ProjectCardInline,
    ]

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
        ("Currículo (somente para a página Currículo)", {
            "fields": ("curriculo_folha_1", "curriculo_folha_2", "curriculo_pdf"),
        }),
    )

    class Media:
        js = ("admin/js/color_sync.js",)


# ======================================================
# ADMIN — CONTATO (DADOS EXTRA)
# ======================================================
@admin.register(ContactContent)
class ContactContentAdmin(admin.ModelAdmin):
    list_display = ("page", "email", "telefone", "updated_at")
