from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from property.models import Category
from website.models import Website
from website.serializers import WebsiteListSerializer


class WebsiteListView(ListAPIView):
    serializer_class = WebsiteListSerializer
    lookup_url_kwarg = 'categoryId'

    def get_queryset(self):
        category_id = self.request.query_params.get(self.lookup_url_kwarg)
        category = Category.objects.filter(id=category_id, is_active=True).first()
        return Website.objects.filter(category=category, is_active=True)


class WebsiteListByKeywordView(ListAPIView):
    serializer_class = WebsiteListSerializer

    def get_queryset(self):
        keyword = self.request.query_params['keyword']
        site_list = Website.objects.filter(is_active=True, name__contains=keyword)
        return site_list


class WebsiteListByFreq(ListAPIView):
    serializer_class = WebsiteListSerializer

    def get_queryset(self):
        site_list = Website.objects.filter(is_active=True).order_by('-freq')[:3]
        return site_list
