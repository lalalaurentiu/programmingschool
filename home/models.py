from django.db import models

class HomePost(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=250, unique=True)
    post = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='Posts')

    def __str__(self):
        return self.title

