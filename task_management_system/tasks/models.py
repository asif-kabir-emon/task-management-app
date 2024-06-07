from django.db import models
from categories.models import Category

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
