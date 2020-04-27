# Generated by Django 3.0.5 on 2020-04-27 14:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0005_recordtodo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecordTodo',
            new_name='Record',
        ),
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name': 'RECORD', 'verbose_name_plural': 'RECORDs'},
        ),
        migrations.AlterModelTable(
            name='record',
            table='record',
        ),
    ]
