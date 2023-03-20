from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    
    class Meta:
        model = Job
        fields = ('employer','job_title', 'description', 'requirements', 'location', 'company', 'salary', 'contract','application_link')