# Generated by Django 4.1.7 on 2023-02-26 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_addition_rename_sub_items_catalogcategory_subitems_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='subItem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.addition'),
        ),
    ]
