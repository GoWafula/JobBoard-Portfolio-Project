from django.db import models
from django.conf import settings
from urllib.parse import urlparse

# Create your models here.


#Employer model
from django.contrib.auth.models import User

class Employer(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    company_name = models.CharField(max_length=1000)
    company_description = models.TextField(max_length=2000)

    def __str__(self):
        return self.company_name



class Job(models.Model):
    employer = models.ForeignKey(Employer,on_delete=models.DO_NOTHING)
    job_title = models.CharField(max_length=100, help_text="please enter the job title")
    description = models.TextField(max_length=500, help_text='describe this job')
    requirements = models.TextField(max_length=2000)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    contract_type = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Freelance', 'Freelancer'),
        )

    contract = models.CharField(choices=contract_type, max_length=100, default=None)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    #application_deadline = models.DateField()
    posted_at = models.DateTimeField(auto_now_add=True)
    application_link = models.URLField()

   

    def __str__(self):
        return self.job_title
    
    def url_text(self):
        parsed_url = urlparse(self.application_link)
        return parsed_url.hostname.replace("www.", "") + "/..."
    