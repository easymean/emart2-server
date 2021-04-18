from django.urls import path

from website.views import WebsiteListView, WebsiteListByKeywordView

app_name = "website"

urlpatterns = [
  path("search/", WebsiteListByKeywordView.as_view()),
  path("", WebsiteListView.as_view()),
]
