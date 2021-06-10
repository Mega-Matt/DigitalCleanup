# Generated by Django 3.0.8 on 2021-01-08 09:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_remove_tag_pubdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='PubDate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата публікації'),
            preserve_default=False,
        ),
    ]
