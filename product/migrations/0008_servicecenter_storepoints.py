# Generated by Django 4.1.7 on 2023-02-26 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_questionanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=25)),
                ('mode', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='StorePoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=25)),
            ],
        ),
    ]
