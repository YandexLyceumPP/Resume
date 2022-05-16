# Generated by Django 3.2.13 on 2022-05-16 22:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show', models.BooleanField(default=True, verbose_name='Показать')),
                ('skill', models.CharField(max_length=100, verbose_name='Название')),
                ('text', tinymce.models.HTMLField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='upload/avatars/')),
                ('skills', models.ManyToManyField(to='users.Skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show', models.BooleanField(default=True, verbose_name='Показать')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('value', tinymce.models.HTMLField(verbose_name='Значение')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Факт',
                'verbose_name_plural': 'Факты',
            },
        ),
    ]
