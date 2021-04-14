from rest_framework import serializers

from website.models import Website
from property.serializers import RelationCategorySerializer, RelationStageSerializer


class WebsiteViewSetSerializer(serializers.ModelSerializer):
    category = RelationCategorySerializer(read_only=True)
    stage = RelationStageSerializer(read_only=True)

    class Meta:
        model = Website
        exclude = [
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "category", "stage"]

    def create(self, validated_data):
        request = self.context.get("request")
        website = Website.objects.create(**validated_data)

