{% extends "common/base.html" %}
{% block title %}
    <title>月間集計</title>
{% endblock %}

{% block content %}
    <h1>月間集計</h1>
    {% if item_list %}
        <ul>
        {% for item in item_list %}
            <li><a href="/detail/{{ item.item_id }}/item_edit"></a></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No item</p>
    {% endif %}
{% endblock %}