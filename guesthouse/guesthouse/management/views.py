from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect


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
    fields = ['title', 'description']

    def post(self, request):
        new_title = request.POST['title']
        new_description = request.POST['description']
        product = Product.objects.create(title=new_title, description=new_description)
        user = [request.user,]
        product.worker.set(user)
        product.save()
        return redirect(reverse_lazy('management:index'))
#Update
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product

#Delete
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("management:index")
