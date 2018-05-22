from django.shortcuts import render
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product

#CRUD
# Create your views here.
#RETRIEVE
class ProductListView(LoginRequiredMixin, ListView):
    model = Product

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

#Create
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product

#Udpate
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product

#Delete
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
