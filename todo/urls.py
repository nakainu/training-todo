from django.urls import path
from todo import views


urlpatterns = [
    path('', views.todo_list, name='todo'),
    path('complete/<int:todo_id>/', views.complete, name='complete'),
    path('setting/edit/<int:todo_id>/', views.edit, name='edit'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('record', views.record, name='record'),
    path('setting', views.add_todo, name='todo_setting'),
]
