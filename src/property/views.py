from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from property.models import Category
from property.serializers import CategoryListSerializer, CategoryRetrieveSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryListSerializer


class CategoryRetrieveView(RetrieveAPIView):
    serializer_class = CategoryRetrieveSerializer
    queryset = Category.objects.filter(is_active=True)
    lookup_url_kwarg = "id"
