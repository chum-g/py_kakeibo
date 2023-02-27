{% extends "common/base.html" %}
{% block title %}
    <title>お知らせ</title>
{% endblock %}

{% block content %}
    {% if notification %}
        <div>
            <table>
                <tr><th>{{ notification.notification_title }}</th></tr>
                <tr><th>{{ notification.notification_detail }}</th></tr>
            </table>
        </div>
    {% endif %}
{% endblock %}