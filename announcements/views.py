from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.


class NewsListView(ListView):
    model = Post
    template_name = 'news_list.html'


class NewsDetailView(DetailView):
    model = Post
    template_name = 'news_detail.html'
