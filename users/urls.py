from django.urls import path
from .views import(
    AdminCategoryadd
) 

app_name = 'staff'

urlpatterns = [
    path("category/", AdminCategoryadd.as_view(), name="category")
]