# Generated by Django 3.0.8 on 2021-01-05 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20210104_2214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postpicture',
            old_name='img',
            new_name='image',
        ),
    ]