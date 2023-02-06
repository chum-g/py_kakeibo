# py_kakeibo

# 環境構築
https://self-methods.com/django-docker-easy/

# 開発参考
https://qiita.com/kaki_k/items/511611cadac1d0c69c54
https://qiita.com/gragragrao/items/373057783ba8856124f3

kill `lsof -ti tcp:8000`
python manage.py runserver 8000


# エラー
webコンテナスタートできない
Error invoking remote method 'docker-start-container': Error: (HTTP code 500) server error - Ports are not available: exposing port TCP 0.0.0.0:80 -> 0.0.0.0:0: listen tcp 0.0.0.0:80: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted.
エラーによると、portが他で使用されているようです。
https://qiita.com/Quantum/items/8891fa9c94d03b388555


### コマンド
django-admin startproject [プロジェクト名]
python manage.py startapp [アプリ名]
python -m django --version
kill `lsof -ti tcp:8000`
python manage.py runserver 8000
mysql -u root -p
CREATE DATABASE django;
python manage.py makemigrations
python manage.py migrate クローン後はこれが必要かも

### modelの作成、登録の記事
https://kuma-server.com/create-save/
トランザクションの張り方を勉強

### フォーム
<form action="{% url '[アプリ名]:[urlsのname]' [引数として渡す変数名] %}" method="post">
{% csrf_token %}
<fieldset>
    <legend><h1>{{ question.question_text }}</h1></legend>
    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
</fieldset>
<input type="submit" value="Vote">
</form>

urlsに追記
path('<[変数の型]:[変数名]>/[パス？]/', views.[関数名], name='[簡略の名前*]'),
例１）path('<int:question_id>/vote/', views.vote, name='vote'),
例１）path('<int:question_id>/vote/', views.vote, name='detail_month'),
*URLをhome/からtop-page/に変更しても対応するURLにアクセスできる。DNSの名前<->ipみたいな

### エラー
フォームのactionの指定がおかしくて"Reverse not found"みたいな奴が出た
    まぁ、urlsの修正がほとんど
    誤字等は注意！！