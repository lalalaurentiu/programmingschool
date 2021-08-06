from django.contrib import admin
from .models import HomePost

@admin.register(HomePost)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'post', 'image']
    prepopulated_fields = {'slug': ('title',)}
