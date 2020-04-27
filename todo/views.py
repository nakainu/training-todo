from django.shortcuts import render, redirect
from todo.models import Todo, Record
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
    """
    complete_atに日時を入れる.
    """
    todo = Todo.objects.get(pk=todo_id)
    # 現在の日時を入れる
    todo.complete_at = datetime.datetime.now()
    todo.save()
    record = Record.objects.create(
        title = todo.title,
        times = todo.times,
        complete_at = todo.complete_at,
        user_id = todo.user_id
    )
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
        return redirect('todo_setting')
    else:   
        form = TodoSettingForm()

    # userのtodoの全てのオブジェクトを取得して並べる．
    todos = Todo.objects.filter(user_id = request.user.id).order_by()
    return render(request, 'todo_setting.html', {'form': form, 'todos' : todos})


def delete(request, todo_id):
    """
    削除機能．
    idと一致したレコードの削除をする．
    """
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('todo_setting')


def edit(request, todo_id):
    """
    編集機能．
    idと一致したレコードの編集をする．
    """
    if request.method == 'POST':
        todo = Todo.objects.get(pk=todo_id)
        # instance引数にモデルインスタンスを指定
        form = TodoSettingForm(request.POST or None, instance=todo)

        if form.is_valid():
            # 保存前のModelインスタンスを取得
            todo = form.save(commit=False)
            todo.title = form.cleaned_data['title']
            todo.times = form.cleaned_data['times']
            form.save()
            return redirect('todo_setting')
    else:
        todo = Todo.objects.get(pk=todo_id)
        return render(request, 'edit.html', {'todo': todo})

    
def record(request):
    """
    記録機能．
    complete_atがnull以外のカラムを全て表示．
    """
    complete_todos = Record.objects.filter(user_id = request.user.id).order_by()
    return render(request, 'record.html', {'todos' : complete_todos})