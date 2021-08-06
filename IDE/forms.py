from django import forms
from users.models import Projects


class SaveProjects(forms.ModelForm):
    project_title = forms.CharField()
    project_code = forms.CharField(widget=forms.Textarea(attrs={'id':'code'}))

    class Meta:
        model = Projects
        fields = ['project_title','project_code']
        

class SaveLoadProjects(forms.ModelForm):
    project_code = forms.CharField(widget=forms.Textarea(attrs={'id':'code'}))

    class Meta:
        model = Projects
        fields = ['project_code']




