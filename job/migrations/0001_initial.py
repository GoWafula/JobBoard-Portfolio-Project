# Generated by Django 4.1.7 on 2023-03-14 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=1000)),
                ('company_description', models.TextField(max_length=2000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(help_text='please enter the job title', max_length=100)),
                ('description', models.TextField(help_text='describe this job', max_length=500)),
                ('requirements', models.TextField(max_length=2000)),
                ('company', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('contract', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Freelance', 'Freelancer')], default=None, max_length=100)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('application_link', models.URLField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='job.employer')),
            ],
        ),
    ]
