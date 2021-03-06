# Generated by Django 3.2.3 on 2021-05-17 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('film', '0003_alter_film_link_of_film'),
    ]

    operations = [
        migrations.CreateModel(
            name='searchhistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.CharField(max_length=9000)),
                ('chosen_or_not', models.IntegerField()),
                ('Film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='namefileOfUser', to='film.film')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
