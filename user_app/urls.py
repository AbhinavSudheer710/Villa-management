"""
URL configuration for villa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from . import views
urlpatterns = [
    path('user_register',views.user_register),
    path('user_dashboard',views.user_dashboard),
    path('user_view_properties',views.user_view_properties),
    path('user_schedule_visit/<int:id>',views.user_schedule_visit,name='user_schedule_visit'),
    path('user_view_booking',views.user_view_booking),
    path('user_booking_delete/<int:id>',views.user_booking_delete,name='user_booking_delete'),
    path('user_booking_edit/<int:id>',views.user_booking_edit,name='user_booking_edit'),
    path('user_booking_edit/user_booking_editss/<int:id>',views.user_booking_editss,name='user_booking_editss'),

]
