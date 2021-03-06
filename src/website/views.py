from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from property.models import Category
from website.models import Website
from website.serializers import WebsiteListSerializer, ReadWebsiteSerializer


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


@api_view(["PUT"])
def freq_increase(request, id):
    try:
        site = Website.objects.get(id=id)
        return Response(ReadWebsiteSerializer(site).data)
    except Website.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)