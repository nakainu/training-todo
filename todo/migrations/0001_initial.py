# Generated by Django 3.0.5 on 2020-04-21 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='ユーザー名')),
                ('email', models.EmailField(max_length=255, verbose_name='パスワード')),
                ('password', models.CharField(max_length=50, verbose_name='メールアドレス')),
            ],
            options={
                'verbose_name': 'ユーザー',
                'verbose_name_plural': 'ユーザー',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='トレーニング名')),
                ('times', models.PositiveIntegerField(verbose_name='回数')),
                ('done', models.BooleanField(default=False, verbose_name='status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.User')),
            ],
            options={
                'verbose_name': 'TODO',
                'verbose_name_plural': 'TODOs',
                'db_table': 'todo',
            },
        ),
    ]
