from django import forms
from .models import Todo


class TodoSettingForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "times"]