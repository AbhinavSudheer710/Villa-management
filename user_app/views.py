from django.shortcuts import render,redirect
from . models import *
from builder_app . models import *
from admin_app . models import *
from user_app . models import *
# Create your views here.

def user_register(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')

        user = user_details(name=name,email=email,phone=phone,password=password)
        user.save()

    return render(request, 'user_register.html')

def user_dashboard(request):
    return render(request, 'user_dashboard_index.html')

def user_view_properties(request):
    data=Property_Detailss.objects.all()
    return render(request, 'user_property_view.html', {'response':data})


def user_schedule_visit(request , id):
    user_id = request.session['uid']
    user_data = user_details.objects.get(id = user_id)
    property_data = Property_Detailss.objects.get(pk=id)

    book = booking(property_name=property_data.property_name ,property_location=property_data.property_location ,property_price=property_data.property_budget,user_id=user_id ,user_name=user_data.name ,user_phone=user_data.phone, user_email=user_data.email)
    book.save()
    return redirect(user_view_properties)

def user_view_booking(request):
    user = request.session['uid']
    property_detail = booking.objects.filter(user_id = user)
    return render(request , 'user_view_booking.html', {'response':property_detail})

def user_booking_delete(request , id):
    booking_details=booking.objects.get(pk=id)
    booking_details.delete()
    return redirect(user_view_booking)

def user_booking_edit(request ,id):
    book = booking.objects.get(pk=id)
    return render(request , 'user_booking_edit.html', {'response':book})

def user_booking_editss(request,id):
    property = booking.objects.get(pk=id)
    if request.method == 'POST':
        user_name=request.POST.get('name')
        user_phone=request.POST.get('phone')
        user_email=request.POST.get('email')

        book = booking(id=id ,property_name=property.property_name, property_location=property.property_location, property_price=property.property_price,user_id=property.user_id,user_name=user_name,user_phone=user_phone,user_email=user_email)
        book.save()
        return redirect(user_view_booking)

    return redirect(request, 'user_booking_edit.html')