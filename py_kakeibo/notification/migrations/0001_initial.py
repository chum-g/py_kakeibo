# Generated by Django 4.1.6 on 2023-02-13 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_id', models.IntegerField(default=0)),
                ('notification_title', models.CharField(max_length=200)),
                ('notification_detail', models.CharField(max_length=1000)),
                ('notification_start', models.CharField(max_length=200)),
                ('notification_end', models.CharField(max_length=200)),
                ('notification_from_user_id', models.CharField(max_length=200)),
                ('notification_to_user_ids', models.CharField(max_length=200)),
            ],
        ),
    ]
