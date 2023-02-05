# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from .models import Item

# Create your views here.
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
    context = {'latest_item_list': latest_item_list}
    return render(request, 'kakeibo/index.html', context)

# def detail_month(request, date):
def detail_month(request):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % date)
    # try:
    #     item = Item.objects.get(item_id)
    # except Item.DoesNotExist:
    #     raise Http404("Item does not exist")
    # return render(request, 'kakeibo/detail_month.html', {'item': item})
    Item.objects.create(itam_id=0, user_id=0, item_name='スタバ', item_amount=2000, item_memo='新作', item_date='2023-02-05')
    return render(request, 'kakeibo/detail_month.html', {'item': 'WRYYYYYYYYY!!!!!!'})

def regist(request, year, month): # , amount, memo, name
    return render(request, 'kakeibo/detail_month.html', {'item': 'WRY.......'})