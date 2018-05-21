from django.shortcuts import render
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product

# Create your views here.
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
