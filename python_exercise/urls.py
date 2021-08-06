from django.urls import path
from . import views 

app_name = "exercise"

urlpatterns = [
    path('<slug>/', views.Exercise.as_view(), name='exercise'),
]