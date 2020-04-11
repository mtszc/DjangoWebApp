from django.shortcuts import render
from django.http import HttpResponse  # no longer being used
from .models import Post

# Here functions will handle the traffic for the specific routes
# we need to map our url pattern to those functions (we do it in urls.py, which we create by ourself in blog directory)


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)  # it's possible to do it with HttpResponse, but it's shorter that way


def about(request):
    return render(request, 'blog/about.html', {'title': "About"})
