from django import forms

class loginpatientform(forms.Form):
    pid = forms.CharField(max_length=4)
    password = forms.CharField(max_length=214214)
class logindoctorform(forms.Form):
    did=forms.CharField(max_length=4)
    password=forms.CharField(max_length=124124)
class registerpatientform(forms.Form):
    pid=forms.CharField(max_length=4)
    password=forms.CharField(max_length=214124)
    name=forms.CharField(max_length=1125)
class registerdoctorform(forms.Form):
    did=forms.CharField(max_length=4)
    password=forms.CharField(max_length=214124)
    name=forms.CharField(max_length=1125)
