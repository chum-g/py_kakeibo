from django.shortcuts import render
from .models import Item
from django.contrib.auth.decorators import login_required
from django import forms

from datetime import date

# Create your views here.
class ItemEditForm(forms.Form):
    # subject = forms.CharField(max_length=100)
    # message = forms.CharField(max_length=1000)
    # sender = forms.EmailField()

    item_date   = forms.CharField(max_length=100)
    item_amount = forms.CharField(max_length=100)
    item_name   = forms.CharField(max_length=100)
    item_memo   = forms.CharField(max_length=100)

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

@login_required
def item_edit(request, item_id):
    form = ItemEditForm(request.POST or None)
    if form.is_valid():
        # チェック
        item_date   = form.cleaned_data["item_date"]
        item_amount = form.cleaned_data["item_amount"]
        item_name   = form.cleaned_data["item_name"]
        item_memo   = form.cleaned_data["item_memo"]

        item = Item.objects.save(
            itam_id     = item_id, 
            user_id     = 0, # TODO ユーザID取得
            item_date   = item_date,
            item_amount = item_amount, 
            item_name   = item_name, 
            item_memo   = item_memo, 
        )

    item = Item.objects.get(id = item_id)
    initial_values = {
        'item_date'   : item.item_date,
        'item_amount' : item.item_amount, 
        'item_name'   : item.item_name, 
        'item_memo'   : item.item_memo, 
    }
    form = ItemEditForm(initial_values)
    
    action = '/detail/'+str(item_id)+"/item_edit/"

    context = {}
    context["item"]      = item
    context["action"]    = action
    context["user_name"] = request.user.username
    context["form"]      = form
    context["date"]      = date.today()# 日付をpythonの標準ライブラリから取得

    template = "detail/item_edit.vue"
    return render(request, template, context)