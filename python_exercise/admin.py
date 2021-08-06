from django.contrib import admin
from .models import Exercise

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['title','slug','description', 'exercise', 'help']
    prepopulated_fields = {'slug':('title',)}


