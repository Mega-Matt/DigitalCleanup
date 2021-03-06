# Generated by Django 3.0.8 on 2021-06-10 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=80, verbose_name="Ім'я")),
                ('bio', models.TextField(blank=True, max_length=110, verbose_name='Біографія(опціонально)')),
                ('image', models.ImageField(default='gratis-png-icono-de-perfil-icono-de-usuario-simple-thumbnail.png', upload_to='authors_pictures/', verbose_name='картинка профілю')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=1000, verbose_name='Заголовок')),
                ('body', models.TextField(blank=True, verbose_name='Текст')),
                ('PubDate', models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації')),
                ('url', models.SlugField(max_length=160, unique=True, verbose_name='URL')),
                ('draft', models.BooleanField(default=False, verbose_name='Чорновик')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Пости',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=80, verbose_name='Назва')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='PostPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=100, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='posts_pictures/', verbose_name='Зображення')),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Зображення до постів',
                'verbose_name_plural': 'Зображення до постів',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='Tag',
            field=models.ManyToManyField(blank=True, related_name='Post_Tag', to='articles.Tag', verbose_name='Теги'),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ManyToManyField(blank=True, max_length=70, to='articles.Author', verbose_name='Автор'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('body', models.TextField(max_length=5000, verbose_name='Текст')),
                ('PubDate', models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації')),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Post', verbose_name='Пост')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Comment', verbose_name='Батьківський коментар')),
            ],
            options={
                'verbose_name': 'Коментар',
                'verbose_name_plural': 'Коментарі',
            },
        ),
    ]
