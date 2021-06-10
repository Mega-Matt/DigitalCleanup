from django.db import models
from django.urls import reverse


class Tag(models.Model):
    Title = models.CharField('Назва', max_length=80)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Author(models.Model):
    Name = models.CharField("Ім'я", max_length=80)
    bio = models.TextField('Біографія(опціонально)', max_length=110, blank=True)
    image = models.ImageField(verbose_name='картинка профілю', upload_to='authors_pictures/', default='gratis-png-icono-de-perfil-icono-de-usuario-simple-thumbnail.png')

    def __str__(self):
        return self.Name


class Post(models.Model):
    Title = models.CharField('Заголовок', max_length=1000)
    body = models.TextField('Текст', blank=True)
    PubDate = models.DateTimeField('Дата публікації', auto_now_add=True)
    Tag = models.ManyToManyField(Tag, verbose_name='Теги', related_name='Post_Tag', blank=True)
    author = models.ManyToManyField(Author, verbose_name='Автор', blank=True, max_length=70)
    url = models.SlugField('URL', max_length=160, unique=True, blank=False)
    draft = models.BooleanField('Чорновик', default=False)

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'


class PostPicture(models.Model):
    Title = models.CharField('Заголовок', blank=True, max_length=100)
    Post = models.ForeignKey(Post, verbose_name='Пост', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Зображення', upload_to='posts_pictures/')

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'Зображення до постів'
        verbose_name_plural = 'Зображення до постів'


class Comment(models.Model):
    email = models.EmailField()
    author = models.CharField('Автор', max_length=100)
    body = models.TextField('Текст', max_length=5000)
    Post = models.ForeignKey(Post, verbose_name='Пост', on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', verbose_name='Батьківський коментар', null=True, blank=True,  on_delete=models.CASCADE
    )
    PubDate = models.DateTimeField('Дата публікації', auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.Post}'

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
