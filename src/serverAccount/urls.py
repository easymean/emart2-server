from django.urls import path

from property.views import CategoryListView, CategoryRetrieveView, StageListView

app_name = "serverAccount"

urlpatterns = [
  path("stage/", StageListView.as_view()),
  path("<int:id>", CategoryRetrieveView.as_view()),
  path("", CategoryListView.as_view()),
]
