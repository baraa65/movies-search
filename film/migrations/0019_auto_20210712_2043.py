# Generated by Django 3.2 on 2021-07-12 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0018_auto_20210712_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='film',
            name='interact',
        ),
        migrations.RemoveField(
            model_name='film',
            name='review',
        ),
        migrations.RemoveField(
            model_name='film',
            name='search',
        ),
    ]
