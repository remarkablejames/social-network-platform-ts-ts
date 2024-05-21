from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    # create custom manager
    class postManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(published=True)

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    objects = models.Manager()
    posts = postManager()

    def __str__(self):
        return self.title
