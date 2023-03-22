from django.http import HttpResponse
from django.shortcuts import render
import json


menu = [{'title': 'home', 'id': 'MyBtn1', 'url': '\\'},
        {'title': 'about', 'id': 'MyBtn2', 'url': '\\about'},
        {'title': 'contacts', 'id': 'MyBtn3', 'url': '#'}
        ]

news = [{'title': 'news_1'},
        {'title': 'news_2'},
        {'title': 'news_3'}
        ]


posts = [
    {'title': 'post_1'},
    {'title': 'post_2'},
    {'title': 'post_3'}
]


def index(request):
    with open('./myapp1/static/img/post/data.json') as f:
        x = json.load(f)

    params = {
        'title': 'Home page',
        'menu': menu,
        'posts': x
    }
    return render(request, 'index.html', params)


def about(request):
    with open('./myapp1/static/img/about/data_news.json') as f:
        x = json.load(f)

    params = {
        'title': 'about page',
        'menu': menu,
        'news': x
    }
    return render(request, 'about.html', params)
