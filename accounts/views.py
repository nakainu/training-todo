from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm

"""
初期ページ
"""
class Index(TemplateView):
    template_name = 'index.html'

"""
アカウントの作成
UserCreationFormクラスで新しいユーザを作成する
"""
class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = "/"
