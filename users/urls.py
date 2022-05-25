from django.urls import path
from .views import(
    AdminCategoryadd,
    EditLessons
) 

app_name = 'staff'

urlpatterns = [
    path("category/", AdminCategoryadd.as_view(), name="category"),
    path("lessons/<int:id>", EditLessons.as_view(), name="lessons"),
]