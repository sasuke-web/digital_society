"""digitalsociety URL Configuration

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
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('home/',views.home,name="home"), 
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('c-profile/',views.c_profile,name='c-profile'),
    path('c-dashboard/',views.c_dashboard,name='c-dashboard'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('reset-password/',views.reset_password,name='reset-password'),
    path('add-member/',views.add_member,name='add-member'),
    path('all-members/',views.all_members,name="all-members"),
    path('add-notice/',views.add_notice,name='add-notice'),
    path('all-watchman/',views.all_watchman,name='all-watchman'),
    path('approved/<int:pk>/',views.approved,name='approved'),
    path('rejected/<int:pk>/',views.rejected,name='rejected'),
    path('all-notice/',views.all_notice,name='all-notice'),
    path('del-notice/<int:pk>/',views.del_notice,name='del-notice'),
    path('noticeview-details/<int:pk>/',views.noticeview_details,name='noticeview-details'),
    path('add-event/',views.add_event,name='add-event'),
    path('all-event/',views.all_event,name='all-event'),
    path('del-event/<int:pk>/',views.del_event,name='del-event'),
    path('eventview-details/<int:pk>/',views.eventview_details,name='eventview-details'),
    path('all-notice/',views.all_notice,name='all-notice'),
    path('pending/<int:pk>/',views.pending,name='pending'),
    path('all-complaint/',views.all_complaint,name='all-complaint'),
     path('c-approved/<int:pk>/',views.c_approved,name='c-approved'),

]
