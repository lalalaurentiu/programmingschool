from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import users.models as model
from lessons.models import (
    Category,
    Lessons
)
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from lessons.forms import (
    CategoryAddForm,
    LessonsAddForm
)


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
            context = {
                "categorys":category,
                "categoryForm":categoryForm,
                "lessonsForm":lessonsForm
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

def addLessons(request, category_id):
    lessonsForm = LessonsAddForm(request.POST)
    if request.method == "POST":
        print(lessonsForm.is_valid())
        if lessonsForm.is_valid():
            instance = lessonsForm.save(commit=False)
            instance.category_id = category_id
            instance.save()
        else:
            lessonsForm = LessonsAddForm()
    return redirect("staff:category")

class EditLessons(TemplateView):
    def get(self,request, id):
        template = "admin/admineditlessons.html"
        lessons = Lessons.objects.get(id=id)
        updateLessonsForm = LessonsAddForm(instance = lessons)
        context = {
            "updateLessonsForm":updateLessonsForm
        }
        response = render(request, template, context)
        return response

    def post(self, request, id):
        lessons = Lessons.objects.get(id=id)
        updateLessonsForm = LessonsAddForm(request.POST, instance = lessons)
        if request.method == "POST":
            if updateLessonsForm.is_valid():
                updateLessonsForm.save()
            else:
                updateLessonsForm = LessonsAddForm()
        
        return redirect("staff:addlessons", id=id)
