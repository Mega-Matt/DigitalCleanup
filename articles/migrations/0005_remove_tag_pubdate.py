# Generated by Django 3.0.8 on 2021-01-06 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20210105_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='PubDate',
        ),
    ]