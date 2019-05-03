from django import forms
from testapp.models import Tourist_Registration,Guide_Registration,language_Selection
class Tourist(forms.ModelForm):
    #password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=Tourist_Registration
        fields='__all__'


class Guide(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=Guide_Registration
        fields='__all__'

class Language_Form(forms.ModelForm):
    class Meta():
        model=language_Selection
        fields = '__all__'
