"""prepcamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing),
    path('index',views.home_mba),
    path('index_engg',views.home_engg),
    # path('studentlogin',views.studentsignup_mba),
    # path('studentlogin_engg',views.studentsignup_engg),
    # path('studentlogin_engg',views.studentlogin_engg),
    # path('studentlogin_engg',views.studentlogin_mba),

    path('studentlogin',views.studentlogin_mba),
    path('studentsignup',views.studentsignup_mba),
    path('facultysignup',views.facultysignup_mba),
    path('facultylogin',views.facultylogin_mba),


    path('studentlogin_engg',views.studentlogin_engg),
    path('studentsignup_engg',views.studentsignup_engg),
    path('facultysignup_engg',views.facultysignup_engg),
    path('facultylogin_engg',views.facultylogin_engg),
    path('engineeringform',views.engg_form),

    path('studentdashboard',views.studentdashboard_mba),
    path('studentdashboard_engg',views.student_enggDashboard),
    # path('facultysignup',views.facultysignup_mba),
    # path('facultysignup',views.facultysignup_engg),
    # path('facultylogin',views.facultylogin_mba),
    # path('facultylogin_engg',views.facultylogin_engg),

    path('facultydashboard',views.facultydashboard),
    path('facultydashboard_engg',views.facultydashboard_engg),
    path('mbaform',views.mba_form),
       
    path('mba_result',views.mba_result),
    # path('engg_result',views.)

    path('csv_engg',views.csvupload_engg),
    path('csv_mba',views.csvupload_mba)

]
