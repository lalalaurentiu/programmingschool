from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import users.models as model
from lessons.models import Category
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from lessons.forms import (
    CategoryAddForm,
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
            context = {
                "categorys":category,
                "categoryForm":categoryForm
            }
            response = render(request, template_name, context)
            return response
        else:
            return HttpResponse(status = 401)

    def post(self, request):
        if request.user.is_staff:
            categoryForm = CategoryAddForm(request.POST)
            if request.method == "POST":
                if categoryForm.is_valid():
                    categoryForm.save()
                    return redirect("staff:category")
            else:
                categoryForm = CategoryAddForm()
        else:
            return HttpResponse(status = 401)


        

