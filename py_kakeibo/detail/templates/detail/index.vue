{% extends "common/base.html" %}
{% block title %}
    <title>家計簿</title>
{% endblock %}

{% block content %}
    <h1>家計簿</h1>
    {% if latest_item_list %}
        <ul>
        {% for item in latest_item_list %}
            <li><a href="/detail/{{ item.id }}/item_edit/">{{ item.item_name }}</a></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No items are available.</p>
    {% endif %}
{% endblock %}