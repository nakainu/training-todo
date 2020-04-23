from django.urls import path
from todo import views


urlpatterns = [
    path('setting', views.add_todo, name='todo_setting'),
]
