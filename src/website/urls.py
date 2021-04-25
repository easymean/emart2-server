from django.urls import path

from website import views

app_name = "website"

urlpatterns = [
  path("freq/<int:id>", views.freq_increase),
  path("search/", views.WebsiteListByKeywordView.as_view()),
  path("freq/", views.WebsiteListByFreq.as_view()),
  path("", views.WebsiteListView.as_view()),
]
