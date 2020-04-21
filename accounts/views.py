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

index = Index.as_view()

"""
アカウントの作成
UserCreationFormクラスで新しいユーザを作成する
password1 と password2 が一致するか確認し、検証
"""
class CreateAccount(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password'を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'create.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        return  render(request, 'create.html', {'form': form,})

create_account = CreateAccount.as_view()
