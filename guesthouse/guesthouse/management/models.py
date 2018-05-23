from datetime import date
from django.db import models
from django.urls import reverse

from guesthouse.users import models as user_model

# Create your models here.
MAX_LENGTH = 50
LONG_LENGTH = 500
TODAY = date.today()

class Product(models.Model):
    title = models.TextField(max_length=MAX_LENGTH)
    description = models.TextField(max_length=LONG_LENGTH)
    worker = models.ManyToManyField(user_model.User)

    def __str__(self):
        return self.title

    def total_cost(self):
        sum = 0
        for i in self.projects.all():
            sum += i.total_cost()
        return sum

    def farthest_date(self):
        farthest = TODAY
        for project in self.projects.all():
            far = project.proj_farthest_date()
            if far > farthest:
                farthest = far
        return farthest

    def get_absolute_url(self):
        return reverse("management:detail", args=[int(self.pk)])


class Project(models.Model):
    title = models.TextField(max_length=MAX_LENGTH)
    product = models.ForeignKey(Product, on_delete="CASCADE", related_name="projects")

    def __str__(self):
        return self.title

    def task_count(self):
        sum = 0
        for t in self.tasks.all():
            sum += 1
        return sum

    def resource_count(self):
        sum = 0
        for r in self.resources.all():
            sum += 1
        return sum

    def total_cost(self):
        sum = 0
        for t in self.tasks.all():
            sum+= t.cost
        for r in self.resources.all():
            sum+= r.cost
        return sum

    def proj_farthest_date(self):
        farthest = TODAY
        for t in self.tasks.all():
            if t.due_date > farthest:
                farthest = t.due_date
        return farthest

class Task(models.Model):
    title = models.TextField(max_length=MAX_LENGTH)
    description = models.TextField(max_length=LONG_LENGTH)
    cost = models.DecimalField(decimal_places=2, max_digits=20)
    due_date = models.DateField()
    project = models.ForeignKey(Project, on_delete="CASCADE", related_name="tasks")

    def __str__(self):
        return self.title

class Resource(models.Model):
    name = models.TextField(max_length=MAX_LENGTH)
    description = models.TextField(max_length=LONG_LENGTH)
    project = models.ForeignKey(Project, on_delete="CASCADE", related_name="resources")
    owner = models.ForeignKey(user_model.User, on_delete="CASCADE")
    cost = models.DecimalField(decimal_places=2, max_digits=20)

    def __str__(self):
        return self.name

class Comment(models.Model):
    body = models.TextField(max_length=1000)
    author = models.ForeignKey(user_model.User, on_delete="CASCADE")
    project = models.ForeignKey(Project, on_delete="CASCADE", related_name="comments")

    def __str__(self):
        return self.body
