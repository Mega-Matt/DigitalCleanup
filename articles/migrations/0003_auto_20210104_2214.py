# Generated by Django 3.0.8 on 2021-01-04 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210104_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.CreateModel(
            name='PostPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=100, verbose_name='Заголовок')),
                ('img', models.ImageField(upload_to='posts_pictures/', verbose_name='Зображення')),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Зображення до постів',
                'verbose_name_plural': 'Зображення до постів',
            },
        ),
    ]
