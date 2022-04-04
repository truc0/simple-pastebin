from django import forms


class SnippetForm(forms.Form):
    language = forms.CharField(widget=forms.TextInput)
    code = forms.CharField(widget=forms.Textarea)