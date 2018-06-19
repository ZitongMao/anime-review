# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 10:57
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('japanese_title', models.CharField(max_length=120)),
                ('created_at', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('review', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('TODO', 'To Watch'), ('DOING', 'Watching'), ('DONE', 'Watched')], default='TODO', max_length=5)),
                ('user', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
