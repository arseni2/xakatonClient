from django import forms

class DocumentCheckForm(forms.Form):
    comments = forms.CharField(widget=forms.Textarea)
