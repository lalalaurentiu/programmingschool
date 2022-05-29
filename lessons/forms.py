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

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = ("category", "slug")
