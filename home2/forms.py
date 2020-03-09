from django import forms

class fileuploadform(forms.Form):
    date=forms.CharField()
    files = forms.FileField()
    