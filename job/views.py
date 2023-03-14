from django.shortcuts import render,redirect,HttpResponse
from .models import Job
from .forms import JobForm
# Create your views here.
# a function view to display the jobs list
def job_list(request):
    jobs = Job.objects.all()

    context = {
        'jobs':jobs,
    }
    return render(request, 'jobs/job_list.html', context)

def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs')
        else:
            form = JobForm
            context = {
                'form':form
            }
        return render(request, 'jobs/post_job.html', context)
    return HttpResponse()
    
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
