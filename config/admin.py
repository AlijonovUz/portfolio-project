from django.contrib import admin

from .models import *


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'address')
    list_display_links = ('email',)
    actions_on_top = False

    def has_add_permission(self, request):
        if Data.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_display_links = ('name',)
    actions_on_top = False
    actions_on_bottom = True


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_display_links = ('name',)
    actions_on_top = False
    actions_on_bottom = True