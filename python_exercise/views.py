from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Exercise as ex
from lessons.views import Category

class Exercise(TemplateView):
    template_name = "python_exercise/exercise.html"

    def get(self, request, slug):
        exercise = ex.objects.filter(slug=slug)
        context = {
            'exercise':exercise,
        }
        return render(request, self.template_name, context)


