# Generated by Django 4.2.6 on 2023-11-01 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0006_rename_product_purchaseorderitem_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='items',
        ),
    ]