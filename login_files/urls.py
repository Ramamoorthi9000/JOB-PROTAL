from django.urls import path
from .views import *

app_name='lf'


from . import views
urlpatterns = [

    path('',two_login_page,name="diffrent_login"),
    path('google_login/',google_login),
    path('login_page/',login_page,name="loginn"),
    path('sign_page/',register_page,name="register"),
    
    path('jobhire/',jobhire, name='jobhire'),


    path('logout/',logout_page,name="logo"),

    path('views_job/',views_job,name="job"),

    path('job_update/<int:id>/',job_update,name="job_update"),
    path('job_delete/<int:id>/',job_delete,name="job_delete"),

    





]

