from django.db import models
from django.db.models.deletion import CASCADE
from lessons.models import Lessons
from django.urls import reverse

class Exercise(models.Model):
    category = models.ForeignKey(Lessons, null=True, on_delete=CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    exercise = models.TextField(blank=True)
    help = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('python_exercise:exercise', args=[self.slug])