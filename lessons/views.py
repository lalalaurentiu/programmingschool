from django.shortcuts import render, get_object_or_404
from .models import Category, Lessons, Lesson
from python_exercise.models import Exercise
from django.views.decorators.clickjacking import xframe_options_exempt

categories = Category.objects.all()

#functia pentru lectii

def lessons(request, lesson_slug = None):
    lessons = Lessons.objects.all()
    category_name = None
    if lesson_slug:
        category_name = get_object_or_404(categories, slug=lesson_slug)
        lessons = lessons.filter(category=category_name)
    return render(request, 'lessons/lessons.html', {'lessons':lessons, 'category':category_name, 'categories':categories})

#fuctia pentru content
def lesson(request, slug = None):
    lessons = Lessons.objects.all()
    lessons_content = Lesson.objects.all()
    lesson_name = None
    if slug:
        lesson_name = get_object_or_404(lessons, slug=slug)
        lessons_content = lessons_content.filter(category=lesson_name)
        if str(lesson_name.category) == "Python":
            exercise = Exercise.objects.filter(category = lesson_name)
            return render(request, 'lessons/python_leson.html', {'lessons_content': lessons_content, 'lessons_name':lesson_name, 'categories':categories, 'exercise':exercise})
        else:
            return render(request, 'lessons/html_leson.html', {'lessons_content': lessons_content, 'lessons_name':lesson_name, 'categories':categories})

@xframe_options_exempt
def lesson_code(request, slug = None):
    lessons = Lessons.objects.all()
    lessons_content = Lesson.objects.all()
    lesson_name = None
    if slug:
        lesson_name = get_object_or_404(lessons, slug=slug)
        lessons_content = lessons_content.filter(category=lesson_name)
    return render(request, 'ide/html_ide.html', {'lessons_content': lessons_content, 'lessons_name':lesson_name, 'categories':categories})
            

    

