from django.shortcuts import render, redirect

from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    new_user = User.objects.create(first_name=request.POST['first_name'], 
    last_name=request.POST['last_name'], 
    email=request.POST['email'], 
    password=request.POST['password'])
    request.session['user'] = new_user.first_name
    request.session['id'] = new_user.id
    return redirect('/dashboard')

def dashboard(request):
    if 'user' not in request.session:
        return redirect('/')
    context = {
        'all_jobs': Job.objects.all()
    }
    return render(request, 'dashboard.html', context)

def new_job(request):
    return render(request, "new_job.html")

def create_job(request):
    Job.objects.create(first_name=request.POST['title'], 
    description=request.POST['description'], 
    location=request.POST['location'], 
    category=request.POST['category'])

    return redirect('/dashboard')