# Generated by Django 3.1.2 on 2020-10-18 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_delete_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='intro',
            field=models.TextField(max_length=200, verbose_name='Введение'),
        ),
    ]
