# Generated by Django 3.0.8 on 2021-03-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20210316_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, max_length=110, verbose_name='Біографія(опціонально)'),
        ),
    ]