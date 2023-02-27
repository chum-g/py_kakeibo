from django.shortcuts import render
from .models import Item
from django.contrib.auth.decorators import login_required

from datetime import date

# Create your views here.
@login_required
def index(request):
    latest_item_list = Item.objects.order_by('-item_date')[:5]
    context  = {'latest_item_list': latest_item_list}
    context |= {'user_name': request.user.username}
    return render(request, 'detail/index.vue', context)

# def detail_month(request, date):
@login_required
def detail_month(request):
    item = Item.objects.create(itam_id=0, user_id=0, item_name='スタバ', item_amount=2000, item_memo='新作', item_date='2023-02-05')
    # return render(request, 'detail/edit.vue', {'item': 'WRYYYYYYYYY!!!!!!'})
    context["item"] = item
    return render(request, 'detail/edit.vue', context)

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
def summary_month(request):
    d = date.today()
    year = d.year
    month = d.month
    return summary_month_y_m(request, year, month)

@login_required
def summary_month_y_m(request, year, month):

    item_list = Item.objects.get(id = 1)

    context = {}
    context["item_list"] = item_list
    context["user_name"] = request.user.username
    context["date"]      = date.today()# 日付をpythonの標準ライブラリから取得

    template = "detail/summary_month.vue"
    return render(request, template, context)

@login_required
def summary_year(request):
    d = date.today()
    year = d.year
    return summary_year_y(request, year)

@login_required
def summary_year_y(request, year):

    item_list = Item.objects.get(id = 1)

    context = {}
    context["item_list"] = item_list
    context["user_name"] = request.user.username
    context["date"]      = date.today()# 日付をpythonの標準ライブラリから取得

    template = "detail/summary_year.vue"
    return render(request, template, context)