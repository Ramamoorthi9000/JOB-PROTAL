from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *






def two_login_page(request):
    return render(request,'different_login.html')


def google_login(request):
    return render(request,'google_login.html')



def login_page(request): 
    form = loginForm()
    if request.method =='POST':
      
        form=loginForm(request.POST)
        if form.is_valid():
           
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('job:dash')



    return render(request,'login.html',{'form':form})



def register_page(request):
    form=RegisterForm() 
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
           
            user.save()
            messages.success(request,'you are Resister succesfull.you can login')  
            return redirect('lf:loginn')


    return render(request,'register.html',{'form':form})



def logout_page(request):
    logout(request)
    return redirect('lf:loginn')




@login_required(login_url='lf:diffrent_login')
def jobhire(request):


    if request.method == "POST":
        job_list.objects.create(
            Company=request.POST.get("Company"),
            job_name=request.POST.get("job_name"),
            Location=request.POST.get("Location"),
            Type=request.POST.get("Type"),
            content=request.POST.get("content"),
            Industry=request.POST.get("Industry"),
            Company_Size=request.POST.get("Company_Size"),
            Experience=request.POST.get("Experience"),
            Skills=request.POST.get("Skills"),
            Description=request.POST.get("Description"),
            Website=request.POST.get("Website"),
        )

    return render(request,'./hire_page/hire.html')


def views_job(request):
        
    context={'da':job_list.objects.filter()}
    return render(request,'./hire_page/views_job.html',context)


def job_update(request,id):
    da=job_list.objects.get(id=id)
    if request.method=="POST":
        
        Company=request.POST["Company"]
        job_name=request.POST["job_name"]
        Location=request.POST["Location"]
        Type=request.POST["Type"]
        Industry=request.POST["Industry"]
        Company_Size=request.POST["Company_Size"]
        Experience=request.POST["Experience"]
        Skills=request.POST["Skills"]
        Website=request.POST["Website"]
        content=request.POST["content"]
        Description=request.POST["Description"]
        
        da.Company=Company
        da.job_name=job_name
        da.Location=Location
        da.Type=Type
        da.Industry=Industry
        da.Company_Size=Company_Size
        da.Experience=Experience
        da.Skills=Skills
        da.Website=Website
        da.content=content
        da.Description=Description
        da.save()
        return redirect('lf:job')
        
    return render(request,'./hire_page/job_update.html',{'da':da})


def job_delete(request,id):

    
    da=job_list.objects.get(id=id)
    da.delete()
    return redirect('lf:job')



