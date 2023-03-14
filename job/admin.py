from django.contrib import admin
from .models import Job,Employer

# Register your models here.
admin.site.register(Employer)

@admin.register(Job)

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'location', 'salary')