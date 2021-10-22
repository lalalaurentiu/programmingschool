from django.contrib import admin
from django.urls import path, include
from django .conf.urls.static import static
from django.conf import settings
from users import views as user_views
from users.views import projects, html_css_js_projects , user_logout, UserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('lessons/', include('lessons.urls', namespace='lessons')),
    path('IDE/', include('IDE.urls', namespace='IDE')),
    path('HTMLIDE/', include('HTMLIDE.urls', namespace='HTMLIDE')),
    path('exercise/', include('python_exercise.urls', namespace='python_exercise')),

    #users
    path('register/', user_views.register, name='register'),
    path('login/', UserView.as_view(template_name='user/login.html'), name='login'),
    path('accounts/', include('allauth.urls')),
    path('logout/', user_logout, name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('profile/', user_views.profile, name='profile'),
    path('projects/', projects, name='projects'),
    path('html_css_js_projects/', html_css_js_projects, name='html_css_js_projects'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
