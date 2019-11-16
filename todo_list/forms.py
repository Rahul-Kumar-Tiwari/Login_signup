from django import forms
from .models import list,User


class ListForm(forms.ModelForm):
    class Meta:
        model = list
        fields = ["Email","item","completed"]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["Name","Email","Mobile","Password"]

