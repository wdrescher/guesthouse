from django.urls import path

from . import views

app_name = "management"
urlpatterns = [
    path("", views.ProductListView.as_view(), name="index"),
]
