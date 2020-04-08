from django.urls import path  # copied from django_project
from . import views  # we need to have access to functions from views

# copied from django_project
urlpatterns = [
    path('', views.home, name='blog-home'),  # empty path stays for home route, name should be more specific then home
    path('about/', views.about, name='blog-about'),
]
