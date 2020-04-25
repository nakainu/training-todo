from django.urls import path
from todo import views


urlpatterns = [
    path('', views.todo_list, name='todo'),
    path('complete/<int:todo_id>/', views.complete, name='complete'),
    path('setting', views.add_todo, name='todo_setting'),
]
