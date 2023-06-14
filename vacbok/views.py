from django.shortcuts import render,redirect
from django.contrib.admin.views.decorators import user_passes_test
from django.http import HttpRequest,HttpResponse
from .models import VacCenter,Bookings,MyModel
from django.contrib import messages
from .form import CenterForm,UserForm,ImageUploadForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, time,date

def loginPage(request):

    page='login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username=request.POST.get('username').lower()
        password=request.POST.get('pass')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,'User does not exsit')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect('admin-home')
            else:
                return redirect('home')
        else:
             messages.error(request,'User/password does not exsit')

    context={'page':page}
    return render(request,'vacbok/login_1.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'An error occured during registration')
    return render(request,'vacbok/login_1.html',{'form':form})
    

def home(request):
    cent=VacCenter.objects.all()
    
    check_time()
    c_count=cent.count()
    username = request.user.username
    context={'center':cent,'c_count':c_count,'username':username}
    return render(request,'vacbok/home.html',context)


def check_time():
    current_time = datetime.now().time()
    target_time = time(0,0)  # Specify the target time to check against
    if current_time == target_time:
        for i in VacCenter.objects.all():
            i.slot_coun=10
            i.save()

@login_required(login_url='login')
def booking(request):
    q=request.GET.get('q') if request.GET.get('q')!=None else ''
    check_time()
    cent=VacCenter.objects.filter(cen_name__contains=q)
    context={'center':cent}
    return render(request,'vacbok/booking.html',context)

@login_required(login_url='login')
def myPro(request,pk):
    user=User.objects.get(id=pk)
    context={'user':user}
    
    return render(request,'vacbok/myprofile.html',context)

def center(request,pk):
    centt=VacCenter.objects.get(id=int(pk))
    if request.method=='POST':
        vacname=request.POST.get('vcname')
        current_date = date.today()
        email=request.POST.get('ename')
        formatted_date = current_date.strftime("%Y-%m-%d ")  
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        conumber=request.POST.get('contactnum')
        slotdt=formatted_date+request.POST.get('datetime')
        username = request.user.username
        bookslot=Bookings(username=username,vaccine_center=vacname,first_name=firstname,last_name=lastname,contact_number=conumber,book_date=slotdt,e_mail=email)
        for i in Bookings.objects.all():
            if i.book_date==slotdt or centt.slot_coun==0:
                messages.error(request,'Slot have been booked please try another slot')
                return redirect('booking')
        centt.slot_coun=centt.slot_coun-1
        centt.save()
        print("hello",centt.slot_coun)
        bookslot.save()
        return redirect('home')
    context={'center':VacCenter.objects.get(id=int(pk))}
    return render(request,'vacbok/center.html',context)


def aboutMe(request):
    return render(request,'vacbok/contact.html')


#######################################admin########################################

@login_required(login_url='login')
def adminShow(request):
    cent=VacCenter.objects.all()
    context={'center':cent}
    return render(request,'vacbok/admin/admin-center.html',context)


@login_required(login_url='login')
def addloc(request):
    form=CenterForm()
    if request.method=='POST':
        form=CenterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('centersE')
    context={'form':form}
    return render(request,'vacbok/admin/register_location.html',context)

def updateloc(request,pk):
    center=VacCenter.objects.get(id=pk)
    form=CenterForm(instance=center)

    if request.method=='POST':
        form=CenterForm(request.POST,instance=center)
        if form.is_valid():
            form.save()
            return redirect('centersE')


    context={'form':form}
    return render(request,'vacbok/admin/register_location.html',context)

def delelteCenter(request,pk):
    center=VacCenter.objects.get(id=pk)
    if request.method=='POST':
        center.delete()
        return redirect('centersE')
    return render(request,'vacbok/admin/delete.html',{'obj':center})

def verifica(request,pk):
    center=Bookings.objects.get(id=pk)
    if request.method=='POST':
        center.is_verified=True
        center.save()
        return redirect('abookings')
    return render(request,'vacbok/admin/updates.html',{'obj':center})

def ahome(request):
    cent=VacCenter.objects.all()
    c_count=cent.count()
    username = request.user.username
    context={'center':cent,'c_count':c_count,'username':username}
    return render(request,'vacbok/admin/ahome.html',context)

def abookings(request):
    cent=Bookings.objects.all()
    context={'center':cent}
    return render(request,'vacbok/admin/abookings.html',context)

        
    

def updateUser(request):
    user=request.user
    form=UserForm(instance=user)
    if request.method=='POST':
        form=UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('myprofile', pk=user.id )

    return render(request,'vacbok/update-user.html',{'form':form})


