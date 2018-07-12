# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-12 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_designer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='type',
            field=models.CharField(choices=[('text', 'text'), ('email', 'e-mail address'), ('longtext', 'long text'), ('checkbox', 'checkbox'), ('select', 'select'), ('radio', 'radio'), ('multiple-select', 'multiple select'), ('hidden', 'hidden'), ('recaptcha', 'recaptcha')], max_length=20, verbose_name='type'),
        ),
    ]
