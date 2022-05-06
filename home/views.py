from django.shortcuts import render
from .models import HomePost
from lessons.models import Category


def homepost(request):
    template_name = 'home/posts/home.html'
    post = HomePost.objects.all()
    context = {
        'post':post,
        }
    response = render(request, template_name, context)
    return response

