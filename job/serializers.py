from rest_framework import serializers
from .models import Job,Employer

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields  = ['id','company_name', 'company_description']


class JobSerializer(serializers.ModelSerializer):
    employer = EmployerSerializer(read_only = True)

    class Meta:
        model = Job
        fields = ['id', 'job_title', 'description', 'requirements', 'company', 'location', 'contract', 'salary', 'posted_at', 'application_link', 'employer']


        def create(self,validated_data):
            employer_data = validated_data.pop('employer')
            employer = Employer.objects.create(**employer_data)
            job = Job.objects.create(employer = employer, **validated_data)
            return job
        
        def update(self,instance,validated_data):
            employer_data = validated_data.pop('employer')
            employer = instance.employer
            employer.company_name = employer_data.get('company_name', employer.company_name)
            employer.company_description = employer_data.get('company_description', employer.company_description)
            employer.save()

            instance.job_title = validated_data.get('job_title', instance.job_title)
            instance.description = validated_data.get('description', instance.description)
            instance.requirements = validated_data.get('requirements', instance.requirements)
            instance.company = validated_data.get('company', instance.company)
            instance.location = validated_data.get('location', instance.location)
            instance.contract = validated_data.get('contract', instance.contract)
            instance.salary = validated_data.get('salary', instance.salary)
            instance.posted_at = validated_data.get('posted_at', instance.posted_at)
            instance.application_link = validated_data.get('application_link', instance.application_link)
            instance.save()
            return instance
