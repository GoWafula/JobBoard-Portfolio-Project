from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import Job
from .forms import JobForm
from django.core.paginator import Paginator
# Create your views here.


# a function view to display the jobs list
def job_list(request):
    job = Job.objects.order_by('-posted_at')

    paginator = Paginator(job,2)
    page_number = request.GET.get('page')
    paged_jobs = paginator.get_page(page_number)
    

    context = {
        'job':paged_jobs,
    }
    return render(request, 'jobs/job.html', context)

def single_job(request, job_id):
    single_job = get_object_or_404(Job,pk=job_id)

    context = {
        'single_job':single_job
    }
    return render(request, 'jobs/single_job.html')

#added a job search functionality
from django.db.models import Q #performs advanced searches than filter and exclude, ncan also be used with &, AND

def search(request):
    query = request.GET.get('q')

    if not query:
        # Handle empty query
        jobs = []
    else:
       
        jobs = Job.objects.filter(
            Q(job_title__icontains=query) | 
            Q(company__icontains=query) |
            Q(contract__icontains=query) |
            Q(location__icontains=query) |
            Q(salary__icontains=query)
        )

    context = {
        'jobs': jobs,
        'query': query
    }

    if not jobs:
        # Handle no matching jobs
        context['error'] = f"No jobs found for '{query}'"

    return render(request, 'jobs/job_search.html', context)


# Views to create,update and delete a job by the employer and admin

from django.contrib.auth.decorators import login_required

@login_required
def employer_dashboard(request):
    employer = request.user.employer
    # Get all job postings associated with the logged-in employer
    jobs = Job.objects.filter(employer=employer)
    return render(request, 'jobs/employer_dashboard.html', {'jobs': jobs})


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    
    # Check if the current user is the employer who created the job posting
    if job.employer != request.user:
        return redirect('employer_dashboard')
    
    # If the request method is POST, process the form data
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_detail', pk=pk)
    
    # If the request method is GET, display the job posting details and form
    else:
        form = JobForm(instance=job)
        
    return render(request, 'jobs/job_detail.html', {'job': job, 'form': form})



@login_required(login_url="login")
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job =form.save(commit=False)
            job.save()
            return redirect('job_detail',pk=job.pk)
    else:
        form = JobForm
    return render(request, 'jobs/post_job.html', {'form': form})

# Views to create,update and delete a job by the employer and admin
def update_job(request,pk):
    job = get_object_or_404(Job,pk = pk)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_detail', pk = job.pk)
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/job_update.html', {'form': form})

# Views to create,update and delete a job by the employer and admin

@login_required(login_url="login")
def job_delete(request, pk):
    profile = request.user
    job = get_object_or_404(Job, id=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('employer_dashboard')
    return render(request, 'jobs/job_delete.html', {'job': job})



# API Views

from rest_framework import generics
from .serializers import EmployerSerializer,JobSerializer
from .models import Employer,Job

class EmployerList(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class EmployerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobRead(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDelete(generics.DestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer