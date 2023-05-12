from django.db import models
from django.contrib.auth.models import User


class PostModel(models.Model):
    title = models.CharField('Title', max_length=120)
    content = models.TextField('Content')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self) -> str:
        return self.title
