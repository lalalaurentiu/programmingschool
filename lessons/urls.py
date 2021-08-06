from django.urls import path
from . import views 



app_name = 'lessons'

urlpatterns = [
    
    path('<slug:lesson_slug>/', views.lessons, name='lessons_category'),
    path('<slug:slug>', views.lesson, name='lessons_detail'),
    path('code/<slug:slug>', views.lesson_code, name='lessons_code'),
]