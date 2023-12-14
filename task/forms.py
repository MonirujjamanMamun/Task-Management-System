from django import forms
from .models import TaskMode


class AddTaskForms(forms.ModelForm):
    class Meta:
        model = TaskMode
        fields = "__all__"
