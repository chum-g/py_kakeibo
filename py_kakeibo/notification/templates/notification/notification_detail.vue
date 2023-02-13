aiueo~
{{user_name}}
{% if notification %}
    <div>
        <table>
            <tr><th>{{ notification.notification_title }}</th></tr>
            <tr><th>{{ notification.notification_detail }}</th></tr>
        </table>
    </div>
    <div>
        <a href="{{request.META.HTTP_REFERER}}">前のページに戻る</a>
    </div>
{% endif %}