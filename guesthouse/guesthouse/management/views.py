from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect


from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product, Project

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
    fields = ['title', 'description']

#Delete
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("management:index")

#------------------------------
#PROJECTS
#------------------------------

#Create
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title']

    def post(self, request, product_k):
        new_title = request.POST['title']
        product_set = Product.objects.filter(pk = product_k)
        for p in product_set:
            product = p
        project = Project.objects.create(title=new_title, product=product)
        return redirect(reverse_lazy('management:project_detail', args=[project.pk]))

#Retrieve
class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project

#Update
class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project

#Delete
class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy("management:index")
