# Generated by Django 3.2.13 on 2022-05-24 23:59

from django.db import migrations, models
import workshop.validators


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0002_alter_block_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'ordering': ('order',), 'verbose_name': 'Блок', 'verbose_name_plural': 'Блоки'},
        ),
        migrations.RemoveField(
            model_name='block',
            name='show',
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact',
            field=models.CharField(max_length=1000, validators=[workshop.validators.OrReValidator(('[a-zA-Z0-9_]+@[a-zA-Z0-9_]+.[a-z0-9]+', '\\+?1?\\d{8,15}', 'https?://[a-zA-Z0-1\\.]+.[a-zA-Z0-1\\:\\.]+(/[a-zA-Z0-1]+)*/?'))], verbose_name='Номер телефона | Email | URL'),
        ),
    ]
