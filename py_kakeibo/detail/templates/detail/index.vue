{% extends "common/base.html" %}
{% block title %}
    <title>家計簿</title>
{% endblock %}

{% block content %}
    {% if latest_item_list %}
        <ul>
        {% for item in latest_item_list %}
            <li><a href="/kakeibo/{{ item.id }}/">{{ item.item_name }}</a></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No items are available.</p>
    {% endif %}
    <div>
        <a href="{{request.META.HTTP_REFERER}}">前のページに戻る</a>
    </div>
{% endblock %}