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
        exclude = ("category",)
        widgets = {
            "title":forms.TextInput(attrs={
                "class":"form-control"
            }),
            "content":forms.Textarea(attrs={
                "cols":10, 
                "rows":3,
                "class":"form-control md-textarea"
            }),
            "code_python":forms.Textarea(attrs={
                "cols":10, 
                "rows":3,
                "class":"form-control md-textarea"
            }),
            "code_html":forms.Textarea(attrs={
                "cols":10, 
                "rows":3,
                "class":"form-control md-textarea"
            }),
            "code_css":forms.Textarea(attrs={
                "cols":10, 
                "rows":3,
                "class":"form-control md-textarea"
            }),
            "code_js":forms.Textarea(attrs={
                "cols":10, 
                "rows":3,
                "class":"form-control md-textarea"
            }),
            "code_link":forms.TextInput(attrs={
                "class":"form-control"
            }),
            "video":forms.TextInput(attrs={
                "class":"form-control"
            }),
            "slug":forms.TextInput(attrs={
                "class":"form-control"
            }),
        }
