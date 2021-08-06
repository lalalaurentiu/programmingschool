from django.shortcuts import render
from .models import HomePost
from lessons.models import Category


def homepost(request):
    post = HomePost.objects.all()
    categories = Category.objects.all()
    return render(request, 'home/posts/home.html', {'post':post, 'categories':categories})

