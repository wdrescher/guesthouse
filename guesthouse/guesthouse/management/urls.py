from django.urls import path

from . import views

app_name = "management"
urlpatterns = [
    path("", views.ProductListView.as_view(), name="index"),
    path("detail/<pk>", views.ProductDetailView.as_view(), name="detail"),
    path("pcreate/", views.ProductCreateView.as_view(), name='product_create'),
    path("pupdate/<pk>", views.ProductUpdateView.as_view(), name="product_update"),
    path('pdelete/<pk>', views.ProductDeleteView.as_view(), name="product_delete"),
    path('projcreate/<product_k>', views.ProjectCreateView.as_view(), name='project_create'),
    path('projdetail/<pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('projupdate/<pk>', views.ProjectUpdateView.as_view(), name='project_update'),
    path('projdelete/<pk>', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('taskcreate/<project>', views.TaskCreateView.as_view(), name='task_create'),
    path('taskdetail/<pk>', views.TaskDetailView.as_view(), name='task_detail'),
    path('taskupdate/<pk>', views.TaskUpdateView.as_view(), name='task_update'),
    path('taskdelete/<pk>', views.TaskDeleteView.as_view(), name='task_delete'),
    path('resourcecreate/<project>', views.ResourceCreateView.as_view(), name='resource_create'),
    path('resourcedetail/<pk>', views.ResourceDetailView.as_view(), name='resource_detail'),
    path('resourceupdate/<pk>', views.ResourceUpdateView.as_view(), name='resouce_update'),
    path('resourcedelete/<pk>', views.ResourceDeleteView.as_view(), name='resource_delete'),
]
