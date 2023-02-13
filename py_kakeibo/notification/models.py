from django.db import models

# Create your models here.
class Notification(models.Model):
    notification_id     = models.IntegerField(default=0)
    notification_title  = models.CharField(max_length=200)
    notification_detail = models.CharField(max_length=1000)
    notification_start  = models.CharField(max_length=200)
    notification_end    = models.CharField(max_length=200)
    
    notification_from_user_id = models.CharField(max_length=200)
    notification_to_user_ids  = models.CharField(max_length=200)