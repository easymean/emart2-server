from rest_framework.generics import ListAPIView

from property.models import Category
from property.serializers import CategoryViewSetSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryViewSetSerializer