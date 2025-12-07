from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q
from .models import job_list   # adjust model name if different









def job_list_view(request):
    query = request.GET.get("q", "")

    if query:
        details = job_list.objects.filter(
            Q(Company__icontains=query) |
            Q(Location__icontains=query) |
            Q(Type__icontains=query) |
            Q(Skills__icontains=query)
        ).distinct()
    else:
        details = job_list.objects.all()

    return render(request, "dashboard.html", {
        "details": details,
        "query": query,  # optional: to keep search text in search box
    })



    




@login_required(login_url='lf:diffrent_login')
def Career_Development_page(request):
    return render(request,'Career_Developmen.html')


@login_required(login_url='lf:diffrent_login')
def about_page(request):
    return render(request,'about.html')





@login_required(login_url='lf:diffrent_login')
def job_details(request):
    return render(request,'./briefy_details/job_details.html')



@login_required(login_url='lf:diffrent_login')
def job_inner_details (request):
    return render(request,'./briefy_details/job_inner_details.html')










@login_required(login_url='lf:diffrent_login')
def dashboard_page(request):
    job=job_list.objects.all()
    context={'details':job}
    return render(request,'dashboard.html',context)


@login_required(login_url='lf:diffrent_login')
def apply_job(request,id):
    job=job_list.objects.filter(id=id)
    context={'details':job}
    return render(request,'job_inner.html',context)



@login_required(login_url='lf:diffrent_login')
def job_inner (request):

    return render(request,'job_inner.html')




@login_required(login_url='lf:diffrent_login')
def profile_page(request):
    profile=employee_profile()
    profile, created = employee_profile.objects.get_or_create(
        login_reference=request.user
    )
    return render(request, "profile.html", {"pd": profile})

@login_required
def update_profile(request):

    profile, created = employee_profile.objects.get_or_create(
        login_reference=request.user
    )

    if request.method == 'POST':

        # Correct image handling
        if "image" in request.FILES:
            profile.image = request.FILES["image"]
           


        profile.name = request.POST.get('name')
        profile.professional = request.POST.get('professional')
        profile.email = request.POST.get('email')
        profile.number = request.POST.get('number')
        profile.location = request.POST.get('location')
        profile.skills = request.POST.get('skills')
        profile.work_experience = request.POST.get('work_experience')
        profile.education = request.POST.get('education')
        profile.project = request.POST.get('project')

        profile.save()
        return redirect('job:profile_page')

    return render(request, 'update_profile.html', {"pd": profile})


def delete_profile (request):
        
    return render(request, 'update_profile.html')

