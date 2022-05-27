from django.urls import path
from .views import(
    AdminCategoryadd,
    deleteCategory,
    EditLessons,
    addLessons,
    deleteLessons,
) 

app_name = 'staff'

urlpatterns = [
    path("category/", AdminCategoryadd.as_view(), name="category"),
    path("delete_category/<int:id>", deleteCategory, name="deleteCategory"),
    path("edit_lessons/<int:id>", EditLessons.as_view(), name="editlessons"),
    path("add_lessons/<int:category_id>", addLessons, name="addlessons"),
    path("delete_lessons/<int:id>", deleteLessons, name="deletelessons"),
]