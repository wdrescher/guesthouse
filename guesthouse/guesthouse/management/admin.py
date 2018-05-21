from django.contrib import admin
from .models import Product, Project, Task, Resource, Comment
# Register your models here.
admin.site.register(Product)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Resource)
admin.site.register(Comment)
