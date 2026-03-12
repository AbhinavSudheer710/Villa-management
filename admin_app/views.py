from django.shortcuts import render,redirect
from villa.models import *
from . models import *
from user_app.models import *
from builder_app.models import *
# Create your views here.
def admin_dashboard(request):
    user_count=user_details.objects.count()
    builder_count=builder_details.objects.count()
    approved_builder_count=builder_approve.objects.count()
    return render(request,'admin_dashboard_index.html' , {'user_count':user_count,'builder_count':builder_count,'approved_builder_count':approved_builder_count})

def query_display(request):
    data = queries.objects.all()
    return render(request,'query_view.html',{'response':data})

def builder_view(request):
    data = builder_details.objects.all()
    return render(request,'builder_view.html',{'response':data})

def builder_approved(request, id):
    builder_data=builder_details.objects.get(pk=id)
    approved_builder=builder_approve(name=builder_data.name,email=builder_data.email,phone=builder_data.phone,password=builder_data.password)
    approved_builder.save()
    builder_data.delete()
    return redirect(builder_view)

def builder_reject(request,id):
    builder_data = builder_details.objects.get(pk=id)
    builder_data.delete()
    return redirect(builder_view)

def view_schedule_visit(request):
    data = booking.objects.all()
    return render(request , 'admin_schedule_visit_view.html', {'bookings':data})

def user_view(request):
    data = user_details.objects.all()
    return render(request , 'admin_user_view.html' ,{'response':data})