from django.contrib import admin
from todo.models import Todo


class TodoAdmin(admin.ModelAdmin):
    # 一覧表示で表示するフィールドを設定
    list_display = ('title', 'times', 'complete_at', 'user')

admin.site.register(Todo, TodoAdmin)
