from django.shortcuts import render, redirect
from todo.models import Todo
from django.contrib.auth.models import User
from todo.forms import TodoSettingForm
import datetime


def todo_list(request):
    """
    userのtodoの全てのオブジェクトを取得して並べる．
    """
    todos = Todo.objects.filter(user_id = request.user.id).order_by()
    return render(request, 'todo.html', {'todos' : todos})


def complete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    # 現在の日時を入れる
    todo.complete_at = datetime.datetime.now()
    todo.save()
    return redirect('todo')


def uncomplete(request, todo_id):
    # complete_atを消したい
    return redirect('todo')


def add_todo(request):
    """
    formの情報をtodoテーブルに格納．
    ログインしているuser_idと紐付ける．
    """
    # fieldの値が正しいかを検証
    if request.method == "POST":
        form = TodoSettingForm(request.POST or None)
        if form.is_valid():
            todo = Todo.objects.create(
                title = form.cleaned_data['title'],
                times = form.cleaned_data['times'],
                user_id = request.user.id
            )
        return redirect('todo')
    else:   
        form = TodoSettingForm()
    return render(request, 'todo_setting.html', {'form': form})
