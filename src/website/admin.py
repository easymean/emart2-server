from django.contrib import admin
from website import models


@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Basic Info", {"fields": ["name", "url", "dev"]}),
        ("Status", {"fields": ["is_active", "order"]}),
        ("Detail", {"fields": ["category", "stage"]}),
    )

    list_display = ("id", "is_active", "name", "dev", "category", "stage", "created_at", "updated_at")