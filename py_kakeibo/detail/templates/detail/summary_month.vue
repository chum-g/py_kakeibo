{% extends "common/base.html" %}
{% block title %}
    <title>月間集計</title>
{% endblock %}

{% block content %}
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