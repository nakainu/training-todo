from django.db import models

class User(models.Model):
    username = models.CharField("ユーザー名", max_length=50)
    email = models.EmailField("パスワード", max_length=255)
    password = models.CharField("メールアドレス", max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "user"
        verbose_name = "ユーザー"
        verbose_name_plural = "ユーザー"


class Todo(models.Model):
    title = models.CharField("トレーニング名", max_length=50)
    times = models.PositiveIntegerField("回数")
    done = models.BooleanField("status", default=False)
    user = models.ForeignKey("User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "todo"
        verbose_name = "TODO"
        verbose_name_plural = "TODOs"
        