from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.template import loader

from .models import Post, Tag, Author
from .forms import CommentForm


class TagsAuthors:
    def get_tags(self):
        return Tag.objects.all()

    def get_authors(self):
        return Author.objects.all

    def get_Posts(self):
        return Post.objects.filter(draft=False)


def index(request):
    template = loader.get_template('articles/index.html')
    context = None
    return HttpResponse(template.render(context, request))


class PostsListView(TagsAuthors, ListView):
    model = Post
    queryset = Post.objects.filter(draft=False)
    template_name = 'articles/Feed.html'


class PostDetailView(TagsAuthors, DetailView):
    model = Post
    queryset = Post.objects.filter(draft=False)
    slug_field = "url"
    template_name = 'articles/Article.html'


class FilterPost(TagsAuthors, ListView):
    def get_queryset(self):
        queryset = Post.objects.filter(Tag__in=self.request.GET.getlist('Tag'))
        return queryset


class AddComment(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.Post_id = pk
            form.save()
        return redirect('/')
