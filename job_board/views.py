from django.shortcuts import render, HttpResponse
from .models import JobPosting

# Create your views here.
def index(request):
    jobs = JobPosting.objects.filter(is_active=True)
    print(jobs)
    return HttpResponse("<h1>Job Board</h1>")