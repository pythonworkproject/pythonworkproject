from django import forms
from .models import Login

class UserForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"