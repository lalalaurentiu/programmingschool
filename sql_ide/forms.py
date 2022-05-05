from django import forms


class SqlIdeForm(forms.Form):
    interogare = forms.CharField(widget=forms.Textarea(attrs={
        "style":"width:100%;display:block",
        }))
    def __init__(self, *args, **kwargs):
        super(SqlIdeForm, self).__init__(*args, **kwargs)
        self.fields['interogare'].initial = '/* Exemplu de interogare SELECT */\nSELECT * from user;'
