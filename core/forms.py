from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'parent_name',
            'parent_email',
            'student_age',
            'coding_experience',
            'main_goal',
            'consideration_range',
        ]
        widgets = {
            'parent_name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'student_age': forms.NumberInput(attrs={'class': 'form-control'}),
            'coding_experience': forms.Select(attrs={'class': 'form-select'}),
            'main_goal': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'consideration_range': forms.Select(attrs={'class': 'form-select'}),
        }
