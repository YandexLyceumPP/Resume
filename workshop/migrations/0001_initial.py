# Generated by Django 3.2.13 on 2022-05-03 18:06

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(null=True, upload_to='uploads/icons/', verbose_name='Иконка')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.BooleanField(default=True)),
                ('text', tinymce.models.HTMLField(verbose_name='Текст')),
                ('editDate', models.DateField(auto_now_add=True, verbose_name='Дата редактирования')),
                ('tags', models.ManyToManyField(related_name='tags', to='workshop.Tag', verbose_name='Тэги')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='users.profile')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(null=True, upload_to='uploads/icons/', verbose_name='Иконка')),
                ('text', tinymce.models.HTMLField(verbose_name='Текст')),
                ('url', models.CharField(max_length=150, verbose_name='URL')),
                ('approved', models.BooleanField(default=False)),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link_publication', to='workshop.publication')),
            ],
            options={
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/files/')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publication', to='workshop.publication')),
            ],
            options={
                'verbose_name': 'Вложение',
                'verbose_name_plural': 'Вложения',
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(null=True, upload_to='uploads/icons/', verbose_name='Иконка')),
                ('title', models.CharField(max_length=20, verbose_name='Навазние')),
                ('value', models.CharField(max_length=100, verbose_name='Значение')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='users.profile')),
            ],
            options={
                'verbose_name': 'Факт',
                'verbose_name_plural': 'Факты',
            },
        ),
    ]
