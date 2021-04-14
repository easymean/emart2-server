from django.urls import path

from website.views import WebsiteListView

app_name = "website"

urlpatterns = [
  path("", WebsiteListView.as_view())
]
