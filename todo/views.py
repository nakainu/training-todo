from django.shortcuts import render
from todo.models import Todo
from django.contrib.auth.models import User
from todo.forms import TodoSettingForm

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
    else:   
        form = TodoSettingForm()
    return render(request, 'todo_setting.html', {'form': form})
