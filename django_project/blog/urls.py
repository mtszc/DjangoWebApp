from django.urls import path  # copied from django_project
from .views import (  # our classes
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views  # we need to have access to functions from views

# copied from django_project
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),  # empty path stays for home route, name should be more specific then home
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),  # pk stands for primary key
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
