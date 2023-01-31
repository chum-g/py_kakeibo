# Generated by Django 4.1.5 on 2023-01-31 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FixedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixed_itam_id', models.IntegerField(default=0)),
                ('user_id', models.IntegerField(default=0)),
                ('fixed_item_name', models.CharField(max_length=200)),
                ('fixed_item_amount', models.IntegerField(default=0)),
                ('fixed_item_memo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itam_id', models.IntegerField(default=0)),
                ('user_id', models.IntegerField(default=0)),
                ('item_name', models.CharField(max_length=200)),
                ('item_amount', models.IntegerField(default=0)),
                ('item_memo', models.CharField(max_length=200)),
                ('item_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('user_name', models.CharField(max_length=200)),
            ],
        ),
    ]
