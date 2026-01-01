from django.contrib import admin
from django import forms

from .models import Curriculo, SiteTheme


# ======================================================
# WIDGET CUSTOMIZADO: HEX + CAIXINHA DE COR
# ======================================================
class ColorHexWidget(forms.Widget):
    template_name = "admin/widgets/color_hex.html"

    def value_from_datadict(self, data, files, name):
        return data.get(name)


# ======================================================
# FORM DO TEMA (USA O WIDGET CUSTOMIZADO)
# ======================================================
class SiteThemeAdminForm(forms.ModelForm):
    class Meta:
        model = SiteTheme
        fields = "__all__"
        widgets = {
            # MENU
            "menu_color": ColorHexWidget(),

            # HERO / BANNER
            "hero_title_color": ColorHexWidget(),
            "hero_subtitle_color": ColorHexWidget(),

            # SERVIÇOS
            "services_title_color": ColorHexWidget(),
            "services_text_color": ColorHexWidget(),
            "services_border_color": ColorHexWidget(),
            "services_button_color": ColorHexWidget(),

            # PROJETOS
            "projects_title_color": ColorHexWidget(),
            "projects_text_color": ColorHexWidget(),
            "projects_border_color": ColorHexWidget(),
            "projects_button_color": ColorHexWidget(),
        }


# ======================================================
# ADMIN DO TEMA DO SITE
# ======================================================
@admin.register(SiteTheme)
class SiteThemeAdmin(admin.ModelAdmin):
    form = SiteThemeAdminForm
    list_display = ("nome", "pagina", "updated_at")
    list_filter = ("pagina",)
    search_fields = ("nome",)

    fieldsets = (
        ("Identificação", {
            "fields": ("nome", "pagina")
        }),

        ("Menu", {
            "fields": ("menu_color",)
        }),

        ("Hero / Banner", {
            "fields": (
                "hero_title_color",
                "hero_subtitle_color",
            )
        }),

        ("Serviços – Cards", {
            "fields": (
                "services_title_color",
                "services_text_color",
                "services_border_color",
                "services_button_color",
            )
        }),

        ("Projetos – Cards", {
            "fields": (
                "projects_title_color",
                "projects_text_color",
                "projects_border_color",
                "projects_button_color",
            )
        }),
    )

    # 🔹 Carrega o JS que sincroniza HEX ↔ caixinha
    class Media:
        js = ("admin/js/color_sync.js",)


# ======================================================
# ADMIN DO CURRÍCULO
# ======================================================
@admin.register(Curriculo)
class CurriculoAdmin(admin.ModelAdmin):
    list_display = ("titulo_banner", "updated_at")
