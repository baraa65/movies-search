# Generated by Django 3.2.3 on 2021-05-16 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_alter_categories_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('productionCompany', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=9000)),
                ('releaseDate', models.DateField(auto_now_add=True)),
                ('runTime', models.IntegerField()),
                ('spokenLanguage', models.CharField(max_length=100)),
                ('rate', models.IntegerField()),
                ('linkOfFilm', models.CharField(max_length=200)),
                ('Categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='categories.categories')),
            ],
        ),
    ]
