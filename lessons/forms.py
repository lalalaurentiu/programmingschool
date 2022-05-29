from django import forms
from .models import (
    Category,
    Lessons,
    Lesson
)

class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ("slug",)
        widgets = {
            "title":forms.TextInput(attrs={
                "class":"form-control"
            })
        }

class LessonsAddForm(forms.ModelForm):
    class Meta:
        model = Lessons
        exclude = ("category", "slug")
        widgets = {
            "title":forms.TextInput(attrs={
                "class":"form-control"
            }),
            "content":forms.Textarea(attrs={
                "cols":10, 
                "rows":3,
                "class":"form-control md-textarea"
            })
        }

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = ("category", "slug")
