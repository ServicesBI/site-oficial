from django.contrib import admin
from django import forms

from .models import (
    Page,
    PageTheme,
    ServiceCard,
    ProjectCard,
    ContactContent,

    HomePage,
    PythonPage,
    PowerBIPage,
    AutomacoesPage,
    ExcelPage,
    CurriculoPage,
    ContatoPage,
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
# ADMIN BASE (REUTILIZADO POR TODAS AS PÁGINAS)
# ======================================================
class BasePageAdmin(admin.ModelAdmin):
    list_display = ("titulo", "updated_at")
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
        ("Currículo (apenas para a página Currículo)", {
            "fields": ("curriculo_folha_1", "curriculo_folha_2", "curriculo_pdf"),
        }),
    )

    class Media:
        js = ("admin/js/color_sync.js",)


# ======================================================
# REGISTRO DAS PÁGINAS (MENU SEPARADO)
# ======================================================
@admin.register(HomePage)
class HomeAdmin(BasePageAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(slug="home")


@admin.register(PythonPage)
class PythonAdmin(BasePageAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(slug="python")


@admin.register(PowerBIPage)
class PowerBIAdmin(BasePageAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(slug="powerbi")


@admin.register(AutomacoesPage)
class AutomacoesAdmin(BasePageAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(slug="automacoes")


@admin.register(ExcelPage)
class ExcelAdmin(BasePageAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(slug="excel")


@admin.register(CurriculoPage)
class CurriculoPageAdmin(BasePageAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(slug="curriculo")


@admin.register(ContatoPage)
class ContatoPageAdmin(BasePageAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(slug="contato")


# ======================================================
# ADMIN — CONTATO (CONTEÚDO EXTRA)
# ======================================================
@admin.register(ContactContent)
class ContactContentAdmin(admin.ModelAdmin):
    list_display = ("page", "email", "telefone", "updated_at")
