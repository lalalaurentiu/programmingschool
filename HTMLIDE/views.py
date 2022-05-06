from django.shortcuts import render
from users.models import HtmlProject
from HTMLIDE.form import SaveHtmlCssJsProject, LoadHtmlCssJsProject
from django.shortcuts import  render
from lessons.views import Category
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from users.models import Projects
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def html_css_js_ide(request, project_title = None):
    projects = Projects.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'HTMLIDE/html_css_js_ide.html', context)

@xframe_options_exempt
def html_css_js(request):
    return render(request, 'HTMLIDE/html_ide_js.html')


def load_html_css_js(request, project_title):
    projects = HtmlProject.objects.filter(project_title=project_title).first()
    context = {
        "projects":projects,
    }
    return render(request, 'HTMLIDE/load_html_css_js_project.html', context)

login_required
class HtmlCssJsProjectSave(TemplateView):
    template_name = 'HTMLIDE/html_ide_js.html'

    def get(self, request):
        form = SaveHtmlCssJsProject()
        users = User.objects.exclude(id=request.user.id)
        context = {
            'form':form,
            'users':users
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = SaveHtmlCssJsProject(request.POST)
        if form.is_valid():
            title = request.POST.get("project_title")
            html_code = request.POST.get('project_code_html')
            css_code = request.POST.get("project_code_css")
            js_code = request.POST.get("project_code_js")
            user = request.user.id
            HtmlProject.objects.create(project_title = title, project_code_html=html_code, project_code_css=css_code, 
            project_code_js=js_code, user_id=user)
        return HttpResponse("<h1>Proiectul dumneavoastra a fost salvat</h1>")

login_required
class HtmlCssJsProjectLoad(TemplateView):
    def get(self, request, project_title):
        template_name = 'HTMLIDE/load_html_css_js_ide.html'
        projects = HtmlProject.objects.filter(project_title=project_title).first()
        form = LoadHtmlCssJsProject(instance=projects)
        context = {
        'projects': projects,
        'form':form,
        }
        return render(request, template_name, context)

    def post(self, request, project_title):
        projects = HtmlProject.objects.filter(project_title=project_title).first()
        form = LoadHtmlCssJsProject(request.POST, instance=projects)
        if form.is_valid():
            html_code = request.POST.get('project_code_html')
            css_code = request.POST.get("project_code_css")
            js_code = request.POST.get("project_code_js")
            projects = HtmlProject.objects.filter(project_title=project_title).update(project_code_html=html_code, project_code_css=css_code, project_code_js=js_code)
        return HttpResponse("<h1>Proiectul dumneavoastra a fost salvat</h1>")

login_required
def delete_project(request, id):
    if request.method == 'POST':
        projects = HtmlProject.objects.get(id=id)
        projects.delete()
    return HttpResponse("<h1>Proiectul dumneavoastra a fost sters</h1>")

