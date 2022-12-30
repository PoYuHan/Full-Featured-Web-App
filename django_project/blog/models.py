from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # 'auto_now_add' attribute will set now time automatically and you can't modify
    author = models.ForeignKey(User, on_delete = models.CASCADE) # on_delete -> if user is deleted, the post will also be deleted

    def __str__(self) -> str:
        return self.title