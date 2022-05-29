from django import forms
from .models import Exercise

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        exclude = ("category","slug",)
        widgets = {
            "title":forms.TextInput(attrs={
                "class":"form-control"
            }),
            "description":forms.Textarea(attrs={
                "cols":10, 
                "rows":3,
                "class":"form-control md-textarea"
            }),
            "exercise":forms.Textarea(attrs={
                "cols":10, 
                "rows":3,
                "class":"form-control md-textarea"
            }),
            "help":forms.Textarea(attrs={
                "cols":10, 
                "rows":3,
                "class":"form-control md-textarea"
            }),
        }