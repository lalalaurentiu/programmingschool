from django.contrib import admin
from django.urls import path, include, re_path
from django .conf.urls.static import static
from django.conf import settings
from users import views as user_views
from users.views import(
    projects, 
    html_css_js_projects , 
    user_logout, 
    UserView
) 
from django.views.static import serve
from users.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('lessons/', include('lessons.urls', namespace='lessons')),
    path('IDE/', include('IDE.urls', namespace='IDE')),
    path('HTMLIDE/', include('HTMLIDE.urls', namespace='HTMLIDE')),
    path('exercise/', include('python_exercise.urls', namespace='python_exercise')),
    path("sql_ide/", include("sql_ide.urls", namespace="sql_ide")), 

    #users
    path('register/', user_views.register, name='register'),
    path('login/', UserView.as_view(form_class=LoginForm), name='login'),
    path('accounts/', include('allauth.urls')),
    path('logout/', user_logout, name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('profile/', user_views.profile, name='profile'),
    path('projects/', projects, name='projects'),
    path('html_css_js_projects/', html_css_js_projects, name='html_css_js_projects'),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    # staff
    path("staff/", include("users.urls", namespace="staff")),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
