from django.shortcuts import render,redirect
from . models import *
from admin_app.models import *
from user_app . models import *
from builder_app . models import *
from django . contrib import messages

def index(request):
    data = Property_Detailss.objects.all()
    return render(request, 'index.html',{'response':data})
    

def home(request):
    return render(request, 'index.html')

def login(request):
    user_count=user_details.objects.count()
    builder_count=builder_details.objects.count()
    approved_builder_count=builder_approve.objects.count()

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email == 'admin@gmail.com' and password=='admin':
            request.session['email'] = email
            request.session['admin'] = 'admin'
            return render(request , 'admin_dashboard_index.html',  {'user_count':user_count,'builder_count':builder_count,'approved_builder_count':approved_builder_count})

        elif user_details.objects.filter(email=email,password=password).exists():
            user_detailss = user_details.objects.get(email=email,password=password)
            if user_detailss.password == request.POST['password']:
                request.session['uid']=user_detailss.id
                request.session['uname']=user_detailss.name
                request.session['uemail']=user_detailss.email
                request.session['user']='user'
                messages.success(request,"Log-in success")
                return render(request,'user_dashboard_index.html')
        
        elif builder_approve.objects.filter(email=email,password=password).exists():
            approved_builder = builder_approve.objects.get(email=email,password=password)
            if approved_builder.password == request.POST['password']:
                request.session['bid']=approved_builder.id
                request.session['bname']=approved_builder.name
                request.session['bemail']=approved_builder.email
                request.session['builder']='builder'
                messages.success(request,"Log-in success")
                return render(request,'builder_dashboard_index.html')
        else:
            messages.error(request,"Log-in failed")

    return render(request, 'login.html')

def logout(request):
    session_keys=list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(home)




def queries_func(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        queriess = queries(name=name,email=email,subject=subject,message=message)
        queriess.save()
    return render(request , 'index.html')

def builder_register(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')

        user = builder_details(name=name,email=email,phone=phone,password=password)
        user.save()

    return render(request, 'builder_register.html')

def approved_builder(request):
    data = builder_approve.objects.all()
    return render(request, 'approved_builder_view.html',{'response':data})

def builder_delete(request,id):
    data = builder_approve.objects.get(pk=id)
    data.delete()
    return redirect(approved_builder)

