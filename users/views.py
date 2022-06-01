from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from django.contrib import messages

from python_exercise.models import Exercise
from .forms import UserRegisterForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import users.models as model
from lessons.models import (
    Category,
    Lessons,
    Lesson
)
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from lessons.forms import (
    CategoryAddForm,
    LessonsAddForm,
    LessonForm
)
from python_exercise.forms import ExerciseForm


class UserView(LoginView):
    template_name = 'user/login.html'
    categories = Category.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'categories':self.categories})
        return context


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Contul dumneavoastra a fost creat')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, f'V-ati deconectat cu succes')
    return redirect('home:home')

@login_required
def profile(request):
    projects = model.Projects.objects.filter(user_id=request.user.id)
    context = {
        'projects':projects,
    }
    return render(request, 'user/profile.html', context)

@login_required
def projects(request):
    projects = model.Projects.objects.filter(user_id=request.user.id)
    context = {
        'projects':projects,
    }
    return render(request, 'user/user_projects.html', context)

@login_required
def html_css_js_projects(request):
    html_css_js_projects = model.HtmlProject.objects.filter(user_id=request.user.id)
    context = {
        'html_css_js_projects':html_css_js_projects
    }
    return render(request, 'user/html_css_js_projects.html', context)


class AdminCategoryadd(TemplateView):
    def get(self, request):
        if request.user.is_staff:
            template_name = "admin/Category.html"
            category = Category.objects.all()
            categoryForm = CategoryAddForm()
            lessonsForm = LessonsAddForm()
            lessonForm = LessonForm()
            exerciseForm = ExerciseForm()
            context = {
                "categorys":category,
                "categoryForm":categoryForm,
                "lessonsForm":lessonsForm,
                "lessonForm":lessonForm,
                "exerciseForm":exerciseForm
            }
            response = render(request, template_name, context)
            return response
        else:
            return HttpResponse(status = 401)

    def post(self, request):
        if request.user.is_staff:
            if request.method == "POST":
                categoryForm = CategoryAddForm(request.POST)
                if categoryForm.is_valid():
                    categoryForm.save()
                    return redirect("staff:category")
            else:
                categoryForm = CategoryAddForm()
        else:
            return HttpResponse(status = 401)

def deleteCategory(request, id):
    if request.user.is_staff:
        category = Category.objects.get(id=id)
        categoryForm = CategoryAddForm(request.POST)
        if request.method == "POST":
            categoryForm.fields.pop("title")
            if categoryForm.is_valid():
                category.delete()
            else:
                print(categoryForm.errors)
        return redirect("staff:category")
    else:
        return HttpResponse(status = 401)

def addLessons(request, category_id):
    if request.user.is_staff:
        lessonsForm = LessonsAddForm(request.POST)
        if request.method == "POST":
            if lessonsForm.is_valid():
                instance = lessonsForm.save(commit=False)
                instance.category_id = category_id
                instance.save()
            else:
                lessonsForm = LessonsAddForm()
        return redirect("staff:category")
    else:
        return HttpResponse(status = 401)

class EditLessons(TemplateView):
    def get(self,request, id):
        if request.user.is_staff:
            template = "admin/admineditlessons.html"
            lessons = Lessons.objects.get(id=id)
            updateLessonsForm = LessonsAddForm(instance = lessons)
            context = {
                "updateLessonsForm":updateLessonsForm
            }
            response = render(request, template, context)
            return response
        else:
            return HttpResponse(status = 401)

    def post(self, request, id):
        if request.user.is_staff:
            lessons = Lessons.objects.get(id=id)
            updateLessonsForm = LessonsAddForm(request.POST, instance = lessons)
            if request.method == "POST":
                if updateLessonsForm.is_valid():
                    updateLessonsForm.save()
                else:
                    updateLessonsForm = LessonsAddForm()
            return redirect("staff:editlessons", id=id)
        else:
            return HttpResponse(status = 401)

def deleteLessons(request, id):
    if request.user.is_staff:
        lessons = Lessons.objects.get(id=id)
        lessonsForm = LessonsAddForm(request.POST)
        if request.method == "POST":
            lessonsForm.fields.clear()
            if lessonsForm.is_valid():
                lessons.delete()
        return redirect("staff:category")
    else:
        return HttpResponse(status = 401)

def addLesson(request, lessons_id):
    if request.user.is_staff:
        lessonForm = LessonForm(request.POST)
        if request.method == "POST":
            if lessonForm.is_valid():
                instance = lessonForm.save(commit=False)
                instance.category_id = lessons_id
                instance.save()
            else:
                lessonForm = LessonForm()
        return redirect("staff:category")
    else:
        return HttpResponse(status = 401)

class EditLesson(TemplateView):
    def get(self,request, id):
        if request.user.is_staff:
            template = "admin/admineditlesson.html"
            lesson = Lesson.objects.get(id=id)

            lessons_content = Lesson.objects.filter(category=lesson.category.id)
            
            updateLessonForm = LessonForm(instance = lesson)
            context = {
                "updateLessonForm":updateLessonForm,
                "lessons_content":lessons_content,
                "lesson":lesson
            }
            response = render(request, template, context)
            return response
        else:
            return HttpResponse(status = 401)

    def post(self, request, id):
        if request.user.is_staff:
            lessons = Lesson.objects.get(id=id)
            updateLessonForm = LessonForm(request.POST, instance = lessons)
            if request.method == "POST":
                if updateLessonForm.is_valid():
                    updateLessonForm.save()
                else:
                    updateLessonForm = LessonForm()
            return redirect("staff:editlesson", id=id)
        else:
            return HttpResponse(status = 401)

def deleteLesson(request, id):
    if request.user.is_staff:
        lesson = Lesson.objects.get(id=id)
        lessonForm = LessonForm(request.POST)
        if request.method == "POST":
            lessonForm.fields.clear()
            if lessonForm.is_valid():
                lesson.delete()
        return redirect("staff:category")
    else:
        return HttpResponse(status = 401)

def addExercise(request, lessons_id):
    if request.user.is_staff:
        exerciseForm = ExerciseForm(request.POST)
        if request.method == "POST":
            if exerciseForm.is_valid():
                instance = exerciseForm.save(commit=False)
                instance.category_id = lessons_id
                instance.save()
            else:
                exerciseForm = LessonForm()
        return redirect("staff:category")
    else:
        return HttpResponse(status = 401)

class EditExercise(TemplateView):
    def get(self,request, id):
        if request.user.is_staff:
            template = "admin/admineditexercise.html"
            exercise = Exercise.objects.get(id=id)
            updateExerciseForm = ExerciseForm(instance = exercise)
            context = {
                "updateExerciseForm":updateExerciseForm
            }
            response = render(request, template, context)
            return response
        else:
            return HttpResponse(status = 401)

    def post(self, request, id):
        if request.user.is_staff:
            exercise = Exercise.objects.get(id=id)
            updateExerciseForm = ExerciseForm(request.POST, instance = exercise)
            if request.method == "POST":
                if updateExerciseForm.is_valid():
                    updateExerciseForm.save()
                else:
                    updateExerciseForm = ExerciseForm()
            return redirect("staff:editexercise", id=id)
        else:
            return HttpResponse(status = 401)

def deleteExercise(request, id):
    if request.user.is_staff:
        exercise = Exercise.objects.get(id=id)
        exerciseForm = ExerciseForm(request.POST)
        if request.method == "POST":
            exerciseForm.fields.clear()
            if exerciseForm.is_valid():
                exercise.delete()
        return redirect("staff:category")

