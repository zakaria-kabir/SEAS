"""seas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include
from seasapp import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.loginview, name='loginpage'),
    path('logout', views.logoutview, name='logoutpage'),
    path('', views.homeview, name='loginpage'),

    path('view_classroom_requirement_course_offer',
        views.view_classroom_requirement_course_offer, name='view_classroom_requirement_course_offer'),
    path('view_enrolment_course_school',
         views.view_enrolment_course_school, name='view_enrolment_course_school'),
    path('view_revenue_of_iub',
         views.view_revenue_of_iub, name='view_revenue_of_iub'),
    path('view_rev_change',
         views.view_rev_change, name='view_rev_change'),
    path('view_revenue_table_of_iub',
         views.view_revenue_table_of_iub, name='view_revenue_table_of_iub'),
    path('view_sets_rev',
         views.view_sets_rev, name='view_sets_rev'),
    path('view_deptwise_rev_per',
         views.view_deptwise_rev_per, name='view_deptwise_rev_per'),
    path('view_enrolment_details',
         views.view_enrolment_details, name='view_enrolment_details'),
    path('view_usage_resource',
         views.view_usage_resource, name='view_usage_resource'),
    path('view_availabilityvscourse_offer',
         views.view_availabilityvscourse_offer, name='view_availabilityvscourse_offer'),
    path('view_iub_resources',
         views.view_iub_resources, name='view_iub_resources'),
    path('view_engr_school_rev',
         views.view_engr_school_rev, name='view_engr_school_rev'),
    path('uploadfunc',
         views.uploadfunc, name='uploadfunc'),
    path('runpopulationscript',
         views.runpopulationscript, name='runpopulationscript'),

]
