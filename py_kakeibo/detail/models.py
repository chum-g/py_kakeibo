from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(default=0)
    user_name = models.CharField(max_length=200)

class Item(models.Model):
    item_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    item_name = models.CharField(max_length=200)
    item_amount = models.IntegerField(default=0)
    item_memo = models.CharField(max_length=200)
    item_date = models.DateTimeField('date published')

class FixedItem(models.Model):
    # 固定費の項目
    
    fixed_item_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    fixed_item_name = models.CharField(max_length=200)
    fixed_item_amount = models.IntegerField(default=0)
    fixed_item_memo = models.CharField(max_length=200)