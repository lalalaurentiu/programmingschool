from django.shortcuts import(
    render,
    get_object_or_404
) 
from .models import(
    Category, 
    Lessons, 
    Lesson
) 
from python_exercise.models import Exercise
from django.views.decorators.clickjacking import xframe_options_exempt



#functia pentru lectii

def lessons(request, lesson_slug = None):
    lessons = Lessons.objects.all()
    categories = Category.objects.all()
    category_name = None
    if lesson_slug:
        category_name = get_object_or_404(categories, slug=lesson_slug)
        lessons = lessons.filter(category=category_name)

        context = {
            'lessons':lessons, 
            'category':category_name, 
            'categories':categories
            }

    return render(request, 'lessons/lessons.html', context)

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

            context = {
                'lessons_content': lessons_content.order_by("id"),
                'lessons_name':lesson_name,
                'exercise':exercise.order_by("id"),
                'lessons':lessons.filter(category = lesson_name.category).order_by("id"),
                "category":str(lesson_name.category)
                }

            return render(request, 'lessons/python_leson.html', context)
        else:

            context = {
                'lessons_content': lessons_content, 
                'lessons_name':lesson_name, 
                'lessons':lessons.filter(category = lesson_name.category), 
                "category":str(lesson_name.category)
                }

            return render(request, 'lessons/html_leson.html', context)

@xframe_options_exempt
def lesson_code(request, slug = None):
    lessons = Lessons.objects.all()
    lessons_content = Lesson.objects.all()
    lesson_name = None
    if slug:
        lesson_name = get_object_or_404(lessons, slug=slug)
        lessons_content = lessons_content.filter(category=lesson_name)

        context = {
            'lessons_content': lessons_content, 
            'lessons_name':lesson_name,
            }

    return render(request, 'ide/html_ide.html', context)
            

    

