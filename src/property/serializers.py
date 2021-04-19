from rest_framework import serializers

from property.models import Category, Stage


class CategoryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "description")


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name",)


class RelationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class StageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ("id", "name",)


class RelationStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ("name",)



