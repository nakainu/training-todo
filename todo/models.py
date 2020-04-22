from django.contrib.auth import get_user_model
from django.db import models

class Todo(models.Model):
    title = models.CharField("トレーニング名", max_length=50)
    times = models.PositiveIntegerField("回数")
    complete_at = models.DateTimeField('完了日時', null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "todo"
        verbose_name = "TODO"
        verbose_name_plural = "TODOs"
