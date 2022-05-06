from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import users.models as model
from lessons.models import Category
from django.contrib.auth.views import LoginView



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
