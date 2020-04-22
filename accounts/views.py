from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class Index(TemplateView):
    """
    初期ページ
    """
    template_name = 'index.html'


class SignUp(CreateView):
    """
    アカウントの作成
    form_classはUserCreationFormを利用。
    リクエストした際にsignup.htmlをブラウザに出力。
    成功時に"/"へリダイレクトする。
    """
    model = User
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = "/"
