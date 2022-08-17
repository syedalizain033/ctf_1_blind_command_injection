from django import forms

class FormClass(forms.Form):
    urlCommand = forms.CharField(label="URL", max_length=100, required=True)
