from django.urls import path

from property import views

app_name = "property"

category_list = views.CategoryViewSet.as_view({"get": "list", "post": "create"})
category_detail = views.CategoryViewSet.as_view({"get": "retrieve", "delete": "destroy", "put": "update"})

stage_list = views.StageViewSet.as_view({"get": "list", "post": "create"})
stage_detail = views.StageViewSet.as_view({"get": "retrieve", "delete": "destroy", "put": "update"})
urlpatterns = [
  path("category/", category_list),
  path("category/<int:id>", category_detail),
  path("stage/", stage_list),
  path("stage/<int:id>", stage_detail)
]
