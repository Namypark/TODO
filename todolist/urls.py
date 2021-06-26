from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_item/', views.add_item, name='add_item'),
    path('delete_todo/<int:todo_id>/', views.delete_todo)
]
