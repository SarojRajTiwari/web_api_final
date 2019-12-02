from django.urls import path
from apis.accounts.views import CreateUserAPIView

urlpatterns = [
    path("create/", CreateUserAPIView.as_view(), name="create-accounts"),
]
