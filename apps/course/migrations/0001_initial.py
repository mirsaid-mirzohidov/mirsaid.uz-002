# Generated by Django 3.1.2 on 2020-11-19 05:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=60, unique=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='uploads/%Y_%m_%d/', verbose_name='Фото')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('intro', models.TextField(max_length=200, verbose_name='Введение')),
                ('text', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=60, unique=True, verbose_name='Ссылка')),
                ('draft', models.BooleanField(verbose_name='Черновик')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
