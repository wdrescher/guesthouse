from django.db import models
from guesthouse.users import models as user_model
# Create your models here.
MAX_LENGTH = 200
LONG_LENGTH = 500

class Product(models.Model):
    cost = models.DecimalField(decimal_places=2, max_digits=20)
    title = models.TextField(max_length=MAX_LENGTH)
    description = models.TextField(max_length=LONG_LENGTH)
    worker = models.ManyToManyField(user_model.User)

class Project(models.Model):
    title = models.TextField(max_length=MAX_LENGTH)
    product = models.ForeignKey(Product, on_delete="CASCADE")

class Task(models.Model):
    title = models.TextField(max_length=MAX_LENGTH)
    description = models.TextField(max_length=LONG_LENGTH)
    cost = models.DecimalField(decimal_places=2, max_digits=20)
    due_date = models.DateField()
    project = models.ForeignKey(Project, on_delete="CASCADE")

class Resource(models.Model):
    name = models.TextField(max_length=MAX_LENGTH)
    description = models.TextField(max_length=LONG_LENGTH)
    owner = models.ForeignKey(user_model.User, on_delete="CASCADE")

class Comment(models.Model):
    body = models.TextField(max_length=1000)
    author = models.ForeignKey(user_model.User, on_delete="CASCADE")
    project = models.ForeignKey(Project, on_delete="CASCADE")
