from django.urls import path

from . import views

app_name = "management"
urlpatterns = [
    path("", views.ProductListView.as_view(), name="index"),
    path("detail/<pk>", views.ProductDetailView.as_view(), name="detail"),
    path("pcreate/", views.ProductCreateView.as_view(), name='product_create'),
    path("pupdate/", views.ProductUpdateView.as_view(), name="product_update"),
    path('pdelete/', views.ProductDeleteView.as_view(), name="product_delete"),
]
