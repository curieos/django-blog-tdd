# Generated by Django 2.2.2 on 2019-06-17 03:35

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(default=blog.models.get_current_date_time, primary_key=True, serialize=False),
        ),
    ]
