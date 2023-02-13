aiueo~
{{user_name}}
{% if notification_list %}
    <ul>
    {% for notification in notification_list %}
        <li><a href="/notification/{{ notification.id }}/">{{ notification.notification_title }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No notification are available.</p>
{% endif %}

<div>
    <a href="/detail/{{date|date:"Y"}}/">年間家計簿</a>
</div>
<div>
    <a href="/detail/{{date|date:"Y"}}/{{date|date:"m"}}/">月間家計簿</a>
</div>
<div>
    <a href="/detail/{{date|date:"Y"}}/{{date|date:"m"}}/edit">家計簿入力</a>
</div>
<div>
    <a href="{{request.META.HTTP_REFERER}}">前のページに戻る</a>
</div>