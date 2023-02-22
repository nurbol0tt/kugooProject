# Generated by Django 4.1.7 on 2023-02-19 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_banner_image_remove_banner_place_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ManyToManyField(null=True, related_name='product_image', to='product.mediabanner'),
        ),
        migrations.RemoveField(
            model_name='banner',
            name='place_category',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='status_category',
        ),
        migrations.AddField(
            model_name='banner',
            name='place_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='banner_place_category', to='product.placecategory'),
        ),
        migrations.AddField(
            model_name='banner',
            name='status_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='banner_status_category', to='product.status'),
        ),
    ]
