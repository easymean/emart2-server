from django.contrib import admin

from serverAccount import models


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Basic Info", {"fields": ("server_name", "server_ip", "server_id", "server_password")}),
        ("Status", {"fields": ("is_active", )})
    )

    list_display = ("id", "server_name", "server_ip")
