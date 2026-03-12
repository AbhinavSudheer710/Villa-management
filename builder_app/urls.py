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
    path('builder_dashboard',views.builder_dashboard),
    path('add_property',views.add_property),
    path('admin_property_view',views.admin_property_view),
    path('builder_property_view',views.builder_property_view),
    path('builder_property_edit/<int:id>',views.builder_property_edit,name='builder_property_edit'),
    path('builder_property_edit/builder_property_edits/<int:id>',views.builder_property_edits,name='builder_property_edits'),
    path('builder_property_delete/<int:id>',views.builder_property_delete, name='builder_property_delete'),
]
