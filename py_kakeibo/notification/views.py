from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Notification
from datetime import date

# Create your views here.
@login_required
def notification(request):
    notification_list = Notification.objects.order_by('notification_id')[:5]

    context  = {'notification_list': notification_list}
    context |= {'user_name': request.user.username}

    # context["new_date"] = date.today()# 日付をpythonの標準ライブラリから取得
    context["date"]  = date.today()# 日付をpythonの標準ライブラリから取得

    template = "notification/notification_list.vue"
    return render(request, template, context)

@login_required
def detail(request, notification_id):
    notification = Notification.objects.get(notification_id = 0)

    context  = {'notification': notification}
    context |= {'user_name': request.user.username}

    template = "notification/notification_detail.vue"
    return render(request, template, context)