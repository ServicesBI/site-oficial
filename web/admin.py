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
# WIDGET DE COR
# ======================================================
class ColorHexWidget(forms.Widget):
    template_name = "admin/widgets/color_hex.html"

    def value_from_datadict(self, data, files, name):
        return data.get(name)


# ======================================================
# INLINE TEMA
# ======================================================
class PageThemeInline(admin.StackedInline):
    model = PageTheme
    can_delete = False
    extra = 0
    widgets = {
        "menu_color": ColorHexWidget(),
    }


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
# ADMIN BASE
# ======================================================
class BasePageAdmin(admin.ModelAdmin):
    list_display = ("titulo",)
    inlines = [PageThemeInline, ServiceCardInline, ProjectCardInline]

    fieldsets = (
        ("Conteúdo", {
            "fields": ("titulo", "subtitulo", "texto")
        }),
        ("Banner", {
            "fields": ("banner_image",)
        }),
        ("Currículo (apenas na página Currículo)", {
            "fields": (
                "curriculo_folha_1",
                "curriculo_folha_2",
                "curriculo_pdf",
            )
        }),
    )

    class Media:
        js = ("admin/js/color_sync.js",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(slug=self.slug_fixo)

    def has_add_permission(self, request):
        return False


# ======================================================
# PROXIES (MENU REAL)
# ======================================================
class HomePage(Page):
    class Meta:
        proxy = True
        verbose_name = "Home"
        verbose_name_plural = "Home"


class PythonPage(Page):
    class Meta:
        proxy = True
        verbose_name = "Python"
        verbose_name_plural = "Python"


class PowerBIPage(Page):
    class Meta:
        proxy = True
        verbose_name = "Power BI"
        verbose_name_plural = "Power BI"


class AutomacoesPage(Page):
    class Meta:
        proxy = True
        verbose_name = "Automações"
        verbose_name_plural = "Automações"


class ExcelPage(Page):
    class Meta:
        proxy = True
        verbose_name = "Excel"
        verbose_name_plural = "Excel"


class CurriculoPage(Page):
    class Meta:
        proxy = True
        verbose_name = "Currículo"
        verbose_name_plural = "Currículo"


# ======================================================
# REGISTROS
# ======================================================
@admin.register(HomePage)
class HomeAdmin(BasePageAdmin):
    slug_fixo = "home"


@admin.register(PythonPage)
class PythonAdmin(BasePageAdmin):
    slug_fixo = "python"


@admin.register(PowerBIPage)
class PowerBIAdmin(BasePageAdmin):
    slug_fixo = "powerbi"


@admin.register(AutomacoesPage)
class AutomacoesAdmin(BasePageAdmin):
    slug_fixo = "automacoes"


@admin.register(ExcelPage)
class ExcelAdmin(BasePageAdmin):
    slug_fixo = "excel"


@admin.register(CurriculoPage)
class CurriculoAdmin(BasePageAdmin):
    slug_fixo = "curriculo"


# ======================================================
# CONTATO (SEPARADO)
# ======================================================
@admin.register(ContactContent)
class ContactContentAdmin(admin.ModelAdmin):
    list_display = ("email", "telefone", "updated_at")
# ======================================================
# ORDENAR MENU DO ADMIN (WEB)
# ======================================================
from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    def get_app_list(self, request):
        app_list = super().get_app_list(request)

        for app in app_list:
            if app["app_label"] == "web":
                order = [
                    "Home",
                    "Python",
                    "Power BI",
                    "Automações",
                    "Excel",
                    "Currículo",
                    "Contato",
                ]

                app["models"].sort(
                    key=lambda x: order.index(x["name"])
                    if x["name"] in order
                    else 999
                )

        return app_list


# Aplicar customização
admin.site.__class__ = CustomAdminSite
