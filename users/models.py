from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return f"{self.user.username}"

class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=200)
    project_code = models.TextField()

    def get_absolute_url(self):
        return reverse('IDE:project_load', args=[self.project_title])

class HtmlProject(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    project_title = models.CharField(max_length=200)
    project_code_html = models.TextField()
    project_code_css = models.TextField()
    project_code_js = models.TextField()
    
    def get_absolute_url(self):
        return reverse('HTMLIDE:load_html_ide', args=[self.project_title])

