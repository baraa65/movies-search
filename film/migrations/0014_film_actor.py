# Generated by Django 3.2 on 2021-07-12 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0013_auto_20210712_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='actor',
            field=models.ManyToManyField(through='film.acotors_film', to='film.actors'),
        ),
    ]
