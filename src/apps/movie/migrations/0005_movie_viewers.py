# Generated by Django 4.2.3 on 2023-11-22 11:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0004_usermovierelation'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='viewers',
            field=models.ManyToManyField(related_name='movies', through='movie.UserMovieRelation', to=settings.AUTH_USER_MODEL),
        ),
    ]