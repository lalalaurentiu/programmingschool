from django.db import models
from django.db.models.deletion import CASCADE
from lessons.models import Lessons
from django.urls import reverse
from django.utils.text import slugify

class Exercise(models.Model):
    category = models.ForeignKey(Lessons, null=True,blank=True, on_delete=CASCADE, related_name="exercise")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)
    exercise = models.TextField(blank=True)
    help = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('python_exercise:exercise', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(" ", "_")
        super(Exercise,self).save(*args, **kwargs)