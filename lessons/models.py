from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from embed_video.fields import EmbedVideoField

class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    def get_absolute_url(self):
        return reverse('lessons:lessons_category', args=[self.slug])

    def __str__(self):
        return self.title

class Lessons(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('lessons:lessons_detail', args=[self.slug])

    def __str__(self):
        return self.title

class Lesson(models.Model):
    category = models.ForeignKey(Lessons, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField()
    code_python = models.TextField(blank=True)
    code_html = models.TextField(blank=True)
    code_css = models.TextField(blank=True)
    code_js = models.TextField(blank=True)
    code_link = models.CharField(blank=True, max_length=200)
    video = EmbedVideoField(blank=True)


    def get_absolute_url(self):
        return reverse('lessons:lesson_content', args=[self.slug])

    def __str__(self):
        return self.slug


