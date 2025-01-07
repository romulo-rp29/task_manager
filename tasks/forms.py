from django import forms
from tasks.models import Task


class CreateTaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date"]
        labels = {
            "title": "Título",
            "description": "Descrição",
            "due_date": "Prazo",
        }
        widgets = {
            "title": forms.TextInput(),
            "description": forms.Textarea(attrs={"rows": 1}),
            "due_date": forms.DateInput(attrs={"type": "datetime-local"}),
        }
