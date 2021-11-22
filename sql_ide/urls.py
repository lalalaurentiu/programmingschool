from django.urls import path
from sql_ide.views import SqlIde 

app_name = 'sql_ide'

urlpatterns = [
    path("sql_ide/", SqlIde.as_view(), name="sql_ide")
]