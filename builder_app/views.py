from django.shortcuts import render,redirect
from builder_app . models import *
from admin_app . models import *
# Create your views here.
def builder_dashboard(request):
    return render(request, 'builder_dashboard_index.html')

def add_property(request):
    builder_id = request.session['bid']
    if request.method == 'POST':
        photo=request.FILES['property_photo']
        category=request.POST.get('property_category')
        name=request.POST.get('property_name')
        location=request.POST.get('property_location')
        budget=request.POST.get('property_budget')
        bedrooms=request.POST.get('property_bedrooms')
        bathrooms=request.POST.get('property_bathrooms')
        area=request.POST.get('area')
        floor=request.POST.get('floor')
        parking=request.POST.get('parking')

        property = Property_Detailss(property_photo=photo,builder_id=builder_id,property_category=category,property_name=name,property_location=location,property_budget=budget,bedrooms=bedrooms,bathrooms=bathrooms,area=area,floor=floor,parking=parking)
        property.save()


    return render(request, 'add_property.html')

def admin_property_view(request):
    data = Property_Detailss.objects.all()
    return render(request, 'admin_property_view.html',{'response':data})

def builder_property_view(request):
    builder_id = request.session['bid']
    builder_data = Property_Detailss.objects.filter(builder_id=builder_id)
    return render(request, 'builder_property_view.html',{'response':builder_data})

def builder_property_edit(request , id):
    data = Property_Detailss.objects.get(pk=id)
    return render(request , 'builder_property_edit.html', {'response':data})

def builder_property_edits(request , id):
        builder_id = request.session['bid']
        if request.method == 'POST':
            photo=request.FILES['property_photo']
            category=request.POST.get('property_category')
            name=request.POST.get('property_name')
            location=request.POST.get('property_location')
            budget=request.POST.get('property_budget')
            bedrooms=request.POST.get('property_bedrooms')
            bathrooms=request.POST.get('property_bathrooms')
            area=request.POST.get('area')
            floor=request.POST.get('floor')
            parking=request.POST.get('parking')

            property = Property_Detailss(id=id,property_photo=photo,builder_id=builder_id,property_category=category,property_name=name,property_location=location,property_budget=budget,bedrooms=bedrooms,bathrooms=bathrooms,area=area,floor=floor,parking=parking)
            property.save()
            return redirect(builder_property_view)
        return render(request , 'builder_property_edit.html' )

def builder_property_delete(request , id):
     property = Property_Detailss.objects.get(pk=id)
     property.delete()
     return redirect(builder_property_view)