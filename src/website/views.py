from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from property.models import Category
from website.models import Website
from website.serializers import WebsiteViewSetSerializer


class WebsiteListView(ListAPIView):
    serializer_class = WebsiteViewSetSerializer
    lookup_url_kwarg = 'categoryId'

    def get_queryset(self):
        category_id = self.request.query_params.get(self.lookup_url_kwarg)
        print(category_id)
        category = Category.objects.filter(id=category_id, is_active=True).first()
        return Website.objects.filter(category=category, is_active=True)

