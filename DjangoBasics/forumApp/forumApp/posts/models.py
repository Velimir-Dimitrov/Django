from django.db import models
from forumApp.posts.choices import LanguageChoice
from forumApp.posts.validators import BadLanguageValidator


# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=100
    )

    content = models.TextField(
        validators=[BadLanguageValidator()]
    )

    author = models.CharField(
        max_length=30,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    languages = models.CharField(
        choices=LanguageChoice.choices,
        default=LanguageChoice.OTHER
    )

    image = models.ImageField(
        upload_to='posts_images/',
        blank=True,
        null=True,
    )

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    author = models.CharField(
        max_length=100,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
