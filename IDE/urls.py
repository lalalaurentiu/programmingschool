from django.urls import path
from .views import(
    PythonIde, 
    PythonIdeProject, 
    delete_project
)  

app_name = 'IDE'

urlpatterns = [
    path('python_ide', PythonIde.as_view(), name='python_ide'),
    path('<project_title>', PythonIdeProject.as_view(), name='project_load'),
    path('<id>/', delete_project, name='project_delete'),
]