# Generated by Django 4.1.7 on 2023-02-21 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_valuecharacter_key_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='equipment_category',
        ),
    ]
