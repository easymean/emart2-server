from django.urls import path

from property.views import CategoryListView, CategoryRetrieveView

app_name = "property"

urlpatterns = [
  path("", CategoryListView.as_view()),
  path("<int:id>", CategoryRetrieveView.as_view())
]
