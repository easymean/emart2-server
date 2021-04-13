from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from property.models import Category, Stage
from property.serializers import CategoryViewSetSerializer, StageViewSetSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryViewSetSerializer

    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        category.is_active = False
        category.save()
        return Response(data={"result": True}, status=status.HTTP_204_NO_CONTENT)


class StageViewSet(ModelViewSet):
    queryset = Stage.objects.filter(is_active=True)
    serializer_class = StageViewSetSerializer

    def destroy(self, request, *args, **kwargs):
        stage = self.get_object()
        stage.is_active = False
        stage.save()
        return Response(data={"result": True}, status=status.HTTP_204_NO_CONTENT)
