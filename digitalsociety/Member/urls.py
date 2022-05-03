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
# from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('m_all_members/',views.m_all_members,name="m_all_members"), 
#     path('login/',views.login,name="login"),
#     path('logout/',views.logout,name="logout"),
#     path('c-profile/',views.c_profile,name='c-profile'),
#     path('c-dashboard/',views.c_dashboard,name='c-dashboard'),
#     path('forgot-password/',views.forgot_password,name='forgot-password'),
#     path('reset-password/',views.reset_password,name='reset-password'),
#     path('add-member/',views.add_member,name='add-member'),
    path('m_profile/',views.m_profile,name='m_profile'),
    path('m_all_notice/',views.m_all_notice,name="m_all_notice"),
    path('m_all_notice_details/<int:pk>',views.m_all_notice_details,name="m_all_notice_details"),
    path('m-add-complaint/',views.m_add_complaint,name='m-add-complaint'),
    path('m-all-complaint/',views.m_all_complaint,name='m-all-complaint'),
    path('m-add-event/',views.m_add_event,name='m-add-event'),
    path('m-all-event/',views.m_all_event,name='m-all-event'),
    # path('pending/<int:pk>/',views.pending,name='pending'),
    # path('approved/<int:pk>/',views.,name='approved'),

    path('m-dashboard/',views.m_dashboard,name='m-dashboard'),
]
