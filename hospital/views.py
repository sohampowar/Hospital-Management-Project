from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Patient
from django.db.models import Q


# Create your views here.


def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        u=User.objects.create(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
        u.set_password(password)    
        u.save()
        
        return redirect('login_')
        
    return render(request,'register.html')

def login_(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        u=authenticate(username=username,password=password)
        print(u)
        if u is not None:
            login(request,u)
            return redirect('home')
        else:
            wc=True
            return render(request,'login_.html',{'wc':wc})

    return render(request,'login_.html')


@login_required(login_url='login_')
def patient_list(request):
    if 'q' in request.GET:
        q=request.GET['q']
        print(q)
        all_patients=Patient.objects.filter(Q(name__icontains=q) | Q(age__icontains=q) | Q(gender__icontains=q) | Q(address__icontains=q) | Q(contact__icontains=q) | Q(consulting__icontains=q))
    else:
        all_patients=Patient.objects.all()

    return render(request,'patient_list.html',{'all_patients':all_patients})


@login_required(login_url='login_')
def add_patient(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        gender=request.POST['gender']
        address=request.POST['address']
        contact=request.POST['contact']
        consulting=request.POST['consulting']
        u=Patient.objects.create(name=name,age=age,gender=gender,address=address,contact=contact,consulting=consulting)
        return redirect('patient_list')
    
    return render(request,'add_patient.html')

def edit_patient(request):
    return render(request, 'edit_patient.html')

def logout_(request):
    return redirect('login_')


@login_required(login_url='login_')
def profile(request):
    return render(request,'profile.html')

@login_required
def change_pw(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = request.user

        if not user.check_password(old_password):
            return render(request, 'change_pw.html', {'error': 'Old password is incorrect.'})

        if new_password != confirm_password:
            return render(request, 'change_pw.html', {'error': 'New passwords do not match.'})

        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)  # Keep user logged in
        return render(request, 'change_pw.html', {'success': 'Password updated successfully!'})

    return render(request, 'change_pw.html')

@login_required(login_url='login_')
def up_profile(request):
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        un = request.POST['username']

        user = User.objects.get(username=request.user)
        user.first_name = fn
        user.last_name = ln
        user.email = em
        user.username = un
        user.save()

        return redirect('profile')  # Redirect to your profile page

    return render(request, 'up_profile.html')