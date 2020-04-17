有酸素運動TODO
===

## 詳細
TODOアプリにより自宅でできる有酸素運動を毎日継続し、管理することで、健康管理をすることができる。

## 機能の紹介
- ユーザーログイン
    - ユーザーはログインして全機能を利用できる
- TODO画面
    - トレーニング名一覧を表示
- 有酸素運度設定画面
    - トレーニングと回数を登録
    - 登録されているトレーニングの削除
    - 登録されているトレーニングの編集
- 記録画面
    - カレンダーの表示
    - 全てのトレーニングが終わった日は印がつく

## コードの実行手順
```
$ source venv/bin/activate
$ python3 -m venv vnev
$ pip install -U Django==3.0.x django-debug-toolbar
$ git clone https://github.com/nakainu/training-todo.git
$ cd training-todo
$ python manage.py runserver
```

## 実行に必要なPythonのバージョン
- Python 3.7.7