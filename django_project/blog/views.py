from django.shortcuts import render
from django.http import HttpResponse  # no longer being used

# Here functions will handle the traffic for the specific routes
# we need to map our url pattern to those functions (we do it in urls.py, which we create by ourself in blog directory)

# dummy data for a sec
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)  # it's possible to do it with HttpResponse, but it's shorter that way


def about(request):
    return render(request, 'blog/about.html', {'title': "About"})
