from rest_framework import serializers

from website.models import Website
from property.serializers import RelationCategorySerializer, RelationStageSerializer


class WebsiteListSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.name')
    stage = serializers.IntegerField(source='stage.id')

    class Meta:
        model = Website
        fields = ["id", "name", "dev",  "url", "freq", "stage"]


class ReadWebsiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Website
        fields = ["id", "name", "dev",  "url", "freq"]



