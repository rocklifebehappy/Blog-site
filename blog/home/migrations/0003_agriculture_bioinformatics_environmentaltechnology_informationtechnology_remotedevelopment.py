# Generated by Django 3.2.5 on 2021-07-22 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20210720_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemoteDevelopment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('contents', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('date_published', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InformationTechnology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('contents', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('date_published', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EnvironmentalTechnology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('contents', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('date_published', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bioinformatics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('contents', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('date_published', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Agriculture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('contents', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('date_published', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
