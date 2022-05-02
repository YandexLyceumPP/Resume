# Generated by Django 3.2.13 on 2022-05-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(null=True, upload_to='uploads/icons/', verbose_name='Иконка')),
                ('skill', models.CharField(max_length=30, verbose_name='Название')),
                ('text', models.TextField(max_length=150, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
            },
        ),
    ]
