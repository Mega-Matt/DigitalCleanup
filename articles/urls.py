'''from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.PostsListView.as_view(), name='list'),
    path('filter/', views.FilterPost.as_view(), name='filter'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('comment/<int:pk>/', views.AddComment.as_view(), name='add_comment'),
]
'''
