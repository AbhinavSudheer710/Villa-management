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
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('admin_app.urls')),
    path('',include('user_app.urls')),
    path('',include('builder_app.urls')),
    path('',views.index),
    path('login',views.login),
    path('logout',views.logout),
    path('home',views.home),
    path('query',views.queries_func),
    path('builder_register',views.builder_register),
    path('approved_builder',views.approved_builder),
    path('builder_delete/<int:id>',views.builder_delete,name='builder_delete'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
