from django.urls import path

from serverAccount import views

app_name = "serverAccount"

account_list = views.AccountListViewSet.as_view({"get": "list"})

urlpatterns = [
  path("", account_list),
]
