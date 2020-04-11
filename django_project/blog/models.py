from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()  # text field, better for more text
    date_posted = models.DateTimeField(default=timezone.now)  # don't execute this function
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # on delete, when user is deleted, it's delete all user's comments

    def __str__(self):
        return self.title
