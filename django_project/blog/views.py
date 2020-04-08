from django.shortcuts import render
from django.http import HttpResponse  #

# Here functions will handle the traffic for the specific routes
# we need to map our url pattern to those functions (we do it in urls.py, which we create by ourself in blog directory)


def home(request):
    return HttpResponse('<h1>Blog Home</h1>')


def about(request):
    return HttpResponse('<h1>Blog About</h1>')
