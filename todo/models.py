from django.db import models

class Todo(models.Model):
    title = models.CharField("トレーニング名", max_length=50)
    times = models.PositiveIntegerField("回数")
    complete_at = models.DateTimeField('完了日時', null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "todo"
        verbose_name = "TODO"
        verbose_name_plural = "TODOs"
