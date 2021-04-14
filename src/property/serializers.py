from rest_framework import serializers

from property.models import Category, Stage


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


class RelationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class RelationStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ("name",)



