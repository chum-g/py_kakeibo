# Generated by Django 4.1.6 on 2023-02-13 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fixeditem',
            old_name='fixed_itam_id',
            new_name='fixed_item_id',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='itam_id',
            new_name='item_id',
        ),
    ]
