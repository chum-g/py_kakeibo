{% extends "common/base.html" %}
{% block title %}
    <title>家計簿編集</title>
{% endblock %}

{% block content %}
    <h1>{{ item.item_name }}編集</h1>
    <form type="post" action="{{ action }}">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">送信</button>
    </form>
{% endblock %}


<table>
    <tr><th>日時</th><td><input type='text' name='item_date'   value='{{ item.item_date }}'  ></td></tr>
    <tr><th>名前</th><td><input type='text' name='item_name'   value='{{ item.item_name }}'  ></td></tr>
    <tr><th>金額</th><td><input type='text' name='item_amount' value='{{ item.item_amount }}'></td></tr>
    <tr><th>メモ</th><td><input type='text' name='item_memo'   value='{{ item.item_memo }}'  ></td></tr>
</table>