{% extends "common/base.html" %}
{% block title %}
    <title>年間集計</title>
{% endblock %}

{% block content %}
    <h1>年間集計</h1>
    {% if notification_list %}
        <ul>
        {% for notification in notification_list %}
            <li><a href="/notification/{{ notification.id }}/">{{ notification.notification_title }}</a></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No notification are available.</p>
    {% endif %}
{% endblock %}