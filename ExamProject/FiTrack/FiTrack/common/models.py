from django.db import models

class FAQ(models.Model):
    question = models.CharField(
        max_length=255
    )
    answer = models.TextField(
        blank=True,
        null=True,
        default=''
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"FAQ: {self.question}"