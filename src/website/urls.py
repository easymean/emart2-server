from django.urls import path

from . import views
app_name = "websites"

category_list = views.CategoryViewSet.as_view({"get":"list", "post": "create"})
category_detail = views.CategoryViewSet.as_view({"get": "retrieve", "delete": "destroy", "put": "update"})
urlpatterns = [
    path("category/", category_list),
    path("category/<int:pk>", category_detail),
]