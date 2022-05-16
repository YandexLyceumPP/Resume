# Generated by Django 3.2.13 on 2022-05-16 22:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import workshop.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('show', models.BooleanField(default=True, verbose_name='Показать')),
                ('title', models.CharField(max_length=200, verbose_name='Загаловок')),
            ],
            options={
                'verbose_name': 'Блок',
                'verbose_name_plural': 'Блоки',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=1000, validators=[workshop.validators.OrReValidator(('[a-zA-Z0-9_]+@[a-zA-Z0-9_]+.[a-z0-9]+', '\\+?1?\\d{8,15}', 'https?://[a-zA-Z0-1]+.[a-zA-Z0-1]+(/[a-zA-Z0-1]+)*/?'))], verbose_name='Номер телефона | Email | URL')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show', models.BooleanField(default=True, verbose_name='Показать')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', tinymce.models.HTMLField(verbose_name='Текст')),
                ('block', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='workshop.block')),
            ],
            options={
                'verbose_name': 'Текст',
                'verbose_name_plural': 'Текста',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show', models.BooleanField(default=True, verbose_name='Показать')),
                ('image', models.ImageField(null=True, upload_to='upload/avatars/')),
                ('text', tinymce.models.HTMLField(verbose_name='Описание')),
                ('date_edit', models.DateField()),
                ('contacts', models.ManyToManyField(to='workshop.Contact', verbose_name='Контакты')),
                ('tags', models.ManyToManyField(to='workshop.Tag', verbose_name='Тэги')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Резюме',
                'verbose_name_plural': 'Резюме',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show', models.BooleanField(default=True, verbose_name='Показать')),
                ('file', models.FileField(upload_to='uploads/files/')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.block')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.AddField(
            model_name='block',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.resume'),
        ),
    ]
