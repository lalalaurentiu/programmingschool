from django import forms


class SqlIdeForm(forms.Form):
    inquiry = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Introduceti interogarea", "style":"width:100%;display:block"}))
