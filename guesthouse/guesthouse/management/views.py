from django.shortcuts import render
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from .models import Product

# Create your views here.
class ProductListView(ListView):
    model = Product
