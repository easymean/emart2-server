from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Basic Info", {"fields": ("name", )}),
        ("Status", {"fields": ("is_active", )})
    )

    list_display = ("pk", "name", "is_active")