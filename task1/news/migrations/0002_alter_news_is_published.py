# Generated by Django 4.2.5 on 2023-09-05 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
