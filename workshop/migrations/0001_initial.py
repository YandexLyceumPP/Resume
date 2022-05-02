# Generated by Django 3.2.13 on 2022-05-02 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20220502_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(null=True, upload_to='uploads/icons/', verbose_name='Иконка')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(null=True, upload_to='uploads/icons/', verbose_name='Иконка')),
                ('title', models.CharField(max_length=20, verbose_name='Навазние')),
                ('value', models.CharField(max_length=100, verbose_name='Значение')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='users.profile')),
            ],
            options={
                'verbose_name': 'Факт',
                'verbose_name_plural': 'Факты',
            },
        ),
    ]
