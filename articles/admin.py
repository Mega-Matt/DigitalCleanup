'''from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Tag, Comment, PostPicture
# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'url')
    list_display_links = ("Title",)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ('author', 'email',)


class PostPictureInline(admin.TabularInline):
    model = PostPicture
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src= {obj.image.url} width="100" height="110"')

    get_image.short_description = 'Зображення'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'draft', 'PubDate',  'url')
    list_display_links = ("Title",)
    list_filter = ('PubDate', 'draft',)
    search_fields = ('Title',)
    inlines = [PostPictureInline, CommentInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('Post', 'email', 'author', 'body', 'parent')
# readonly_fields = ('author', 'email',)
    list_display_links = ("author",)
    list_filter = ('Post', 'PubDate')


@admin.register(PostPicture)
class PostPictureAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Post', 'get_image',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src= {obj.image.url} width="50" height="60"')

    get_image.short_description = 'Зображення'


admin.site.site_title = 'DigitalCleanup'
admin.site.site_header = 'DigitalCleanup' '''
