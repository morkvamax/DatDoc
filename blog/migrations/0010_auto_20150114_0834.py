# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_keyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='keywords',
            field=models.ManyToManyField(blank=True, null=True, to='blog.KeyWord'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='keyword',
            name='color',
            field=models.CharField(max_length=300, default='rgb(90,90,90)'),
            preserve_default=True,
        ),
    ]
