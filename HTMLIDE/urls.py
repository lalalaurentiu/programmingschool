from django.urls import path
from .views import(
    HtmlCssJsProjectSave, 
    HtmlCssJsProjectLoad, 
    html_css_js, 
    html_css_js_ide, 
    load_html_css_js, 
    delete_project
) 

app_name = 'HTMLIDE'

urlpatterns = [
    path('html_css_js_ide', html_css_js_ide, name='html_css_js_ide'),
    path('html_ide', HtmlCssJsProjectSave.as_view(), name='html_ide'),
    path('load_html_ide/<project_title>', load_html_css_js, name='load_html_ide'),
    path('<project_title>', HtmlCssJsProjectLoad.as_view(), name='project_load'),
    path('<id>/', delete_project, name='project_delete'),
]