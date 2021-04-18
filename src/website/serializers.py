from rest_framework import serializers

from website.models import Website
from property.serializers import RelationCategorySerializer, RelationStageSerializer


class WebsiteListSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.name')
    # stage = serializers.CharField(source='stage.name')

    class Meta:
        model = Website
        fields = ["id", "name", "dev",  "url", "freq"]



