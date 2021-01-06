from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.db.models import Count, Q
from .models import Category, Tag, Post

# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.is_public and not self.request.user.is_authenticated:
            return obj

class CategoryListView(ListView):
    queryset = Category.objects.annotate(num_posts=Count('post', filter=Q(post__is_public=True)))

class TagListView(ListView):
    queryset = Tag.objects.annotate(num_posts=Count('post', filter=Q(post__is_public=True)))

