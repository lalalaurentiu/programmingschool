from django import forms
from users.models import HtmlProject

class SaveHtmlCssJsProject(forms.ModelForm):
    project_title = forms.CharField()
    project_code_html = forms.CharField(widget=forms.Textarea())
    project_code_css = forms.CharField(widget=forms.Textarea())
    project_code_js = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = HtmlProject
        fields = ['project_title', 'project_code_html', 'project_code_css', 'project_code_js']

class LoadHtmlCssJsProject(forms.ModelForm):
    project_code_html = forms.CharField(widget=forms.Textarea())
    project_code_css = forms.CharField(widget=forms.Textarea())
    project_code_js = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = HtmlProject
        fields = ['project_code_html', 'project_code_css', 'project_code_js']