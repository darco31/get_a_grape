# Generated by Django 3.2 on 2022-07-12 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='location',
        ),
    ]
