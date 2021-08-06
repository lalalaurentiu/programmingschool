
from IDE.forms import SaveProjects, SaveLoadProjects
from django.shortcuts import redirect, render
from lessons.views import Category
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from users.models import Projects
from django.contrib import messages

categories = Category.objects.all()

class PythonIde(TemplateView):
    template_name = 'IDE/python_ide.html'

    def get(self, request):
        form = SaveProjects()
        users = User.objects.exclude(id=request.user.id)
        context = {
            'categories': categories,
            'form': form,
            'users': users
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = SaveProjects(request.POST)
        if form.is_valid():
            title = request.POST.get('project_title')
            code = request.POST.get('project_code')
            user = request.user.id
            Projects.objects.create(project_title=title, project_code=code, user_id=user)
            messages.success(request, f'Proiectul dumneavoastra cu titlul {title} a fost salvat')
        return redirect('projects')

class PythonIdeProject(TemplateView):
    template_name = 'IDE/python_ide_project.html'

    def get(self, request, project_title):
        projects = Projects.objects.filter(project_title=project_title).first()
        form = SaveLoadProjects(instance=projects)
        context = {
        'categories': categories,
        'projects': projects,
        'form':form,
        }
        messages.success(request, f'Proiectul a fost incarcat cu succes')
        return render(request, self.template_name, context)

    def post(self, request, project_title):
        projects = Projects.objects.filter(project_title=project_title).first()
        form = SaveLoadProjects(request.POST ,instance=projects)
        if form.is_valid():
            code = request.POST.get('project_code')
            projects = Projects.objects.filter(project_title=project_title).update(project_code=code)
            messages.success(request, f'Proiectul dumneavoastra a fost salvat')
            return redirect('projects')

def delete_project(request, id):
    if request.method == 'POST':
        projects = Projects.objects.get(id=id)
        projects.delete()
        messages.success(request, f'Proiectul dumneavoastra a fost sters')
    return redirect('projects')





    
        


        

