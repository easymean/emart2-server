from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from property.models import Category, Stage
from property.serializers import CategorySerializer,StageListSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer


class StageListView(ListAPIView):
    queryset = Stage.objects.filter(is_active=True)
    serializer_class = StageListSerializer


class CategoryRetrieveView(RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True)
    lookup_url_kwarg = "id"
