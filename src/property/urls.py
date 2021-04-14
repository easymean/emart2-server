from django.urls import path

from property.views import CategoryListView

app_name = "property"

urlpatterns = [
  path("", CategoryListView.as_view()),
]
