# Generated by Django 4.1.6 on 2023-02-17 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyGo', '0002_faq_product_stock_management'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='staffName',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staffPhoneNumber',
            field=models.CharField(default='', max_length=11),
        ),
    ]