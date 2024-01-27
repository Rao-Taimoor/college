from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from .forms  import Userform,Loginform
from django.contrib.auth import login,authenticate

from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method=='POST':
        form=Userform(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            role=form.cleaned_data['role']
            user =User.objects.create_user(email=email,role=role,password=password)
            user.set_password=password
            user.save()
            messages.success(request,'user is created')
            return redirect('login')


    return render(request,'signup.html',{'form':Userform})


def login(request):
    if request.method == 'POST':
        form =Loginform(request.POST)
        if True:
            email = request.POST['email']
            password = request.POST['password']

            # Authenticate user
            user = authenticate(request, email=email, password=password)

            if user is not None:
                # Log the user in
                login(request, user)
                return HttpResponse('Login successful')
            else:
                return HttpResponse('Invalid login credentials')
    


    form=Loginform()
    return render(request,'login.html',{'form':Loginform})
              

    


            



