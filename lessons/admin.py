from django.contrib import admin
from .models import(
    Category, 
    Lessons, 
    Lesson
) 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ['title','slug', 'content']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title','slug', 'content', 'code_python', 'code_html','code_css','code_js' ,'code_link']
    prepopulated_fields = {'slug': ('title',)}

