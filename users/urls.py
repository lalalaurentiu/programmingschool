from django.urls import path
from .views import(
    AdminCategoryadd,
    EditLessons,
    addLessons
) 

app_name = 'staff'

urlpatterns = [
    path("category/", AdminCategoryadd.as_view(), name="category"),
    path("edit_lessons/<int:id>", EditLessons.as_view(), name="editlessons"),
    path("add_lessons/<int:category_id>", addLessons, name="addlessons"),
]