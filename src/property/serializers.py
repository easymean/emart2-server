from rest_framework import serializers

from property.models import Category, Stage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "description")


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



