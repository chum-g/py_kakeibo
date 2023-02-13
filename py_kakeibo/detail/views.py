# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from .models import Item
from django.contrib.auth.decorators import login_required

from datetime import date

# Create your views here.
@login_required
def index(request):
    # return render(request, 'kakeibo/index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")
    latest_item_list = Item.objects.order_by('-item_date')[:5]
    # output = ', '.join([i.item_name for i in latest_question_list])
    # template = loader.get_template('kakeibo/index.html')
    # context = {
    #     'latest_item_list': latest_item_list,
    # }
    # return HttpResponse(output)
    # return HttpResponse(template.render(context, request))
    context  = {'latest_item_list': latest_item_list}
    context |= {'user_name': request.user.username}
    return render(request, 'detail/index.vue', context)

# def detail_month(request, date):
@login_required
def detail_month(request):
    Item.objects.create(itam_id=0, user_id=0, item_name='スタバ', item_amount=2000, item_memo='新作', item_date='2023-02-05')
    return render(request, 'detail/edit.vue', {'item': 'WRYYYYYYYYY!!!!!!'})

@login_required
def edit(request, year, month): # , amount, memo, name
    submit = ""
    context = {}

    context["item"] = 'WRY.......'
    context["date"] = date.today()# 日付をpythonの標準ライブラリから取得
    if submit:
        template = 'detail/edit.vue'
        return render(request, template, context)

    template = 'detail/edit.vue'
    return render(request, template, context)

@login_required
def summary_month(request, year, month):

    item_list = Item.objects.get(id = 1)

    context = {}
    context["item_list"] = item_list
    context["user_name"] = request.user.username
    context["date"]      = date.today()# 日付をpythonの標準ライブラリから取得

    template = "detail/summary_month.vue"
    return render(request, template, context)

@login_required
def summary_year(request, year):

    item_list = Item.objects.get(id = 1)

    context = {}
    context["item_list"] = item_list
    context["user_name"] = request.user.username
    context["date"]      = date.today()# 日付をpythonの標準ライブラリから取得

    template = "detail/summary_year.vue"
    return render(request, template, context)