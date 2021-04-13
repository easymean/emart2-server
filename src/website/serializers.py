from rest_framework import serializers

from website.models import Category


class CategoryViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = [
            "is_active",
            "created_at",
            "updated_at",
            "description"
        ]
        read_only_fields = ["id", "created_at", "updated_at"]



