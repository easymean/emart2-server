from django.contrib import admin

from property import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Basic Info", {"fields": ("name", "description")}),
        ("Status", {"fields": ("is_active", )})
    )

    list_display = ("id", "name", "is_active", "description", "order")


@admin.register(models.Stage)
class StageAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Basic Info", {"fields": ("name",)}),
        ("Status", {"fields": ("is_active", "order")})
    )

    list_display = ("id", "name", "is_active", "order")