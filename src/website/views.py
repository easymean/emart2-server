from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from website.models import Category
from website.serializers import CategoryViewSetSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryViewSetSerializer

    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        category.is_active = False
        category.save()
        return Response(data={"result": True}, status=status.HTTP_204_NO_CONTENT)
