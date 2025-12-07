from django.urls import path
from .views import *
app_name = 'job'

urlpatterns = [
    path('careerdevelopment/', Career_Development_page),
    path('about/', about_page),
    path('job_details/', job_details),
    path('job_inner_details/', job_inner_details),
    path('dashboard/', dashboard_page, name="dash"),
    path('job_inner/', job_inner, name="job_inner"),
    path('inner/<int:id>/', apply_job, name="inner"),
  
    path('profile/',profile_page, name='profile_page'),
    path('update_profile/',update_profile, name='update_profile'),

    path('list/',job_list_view, name='list'),        # main job list

    path('delete_profile/', delete_profile, name="delete_profile"),




]
