from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from acoounts.forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate,login as django_login,logout as django_logout
from django.contrib import messages
def login(request, *args, **kwargs):
    form=LoginForm()

    if request.method == 'POST':
        next=request.GET.get("next",reverse_lazy("home")) #/recipes 
        form=LoginForm(request.POST)
        if form.is_valid():
          user=authenticate(request,username=form.cleaned_data.get('username'),password=form.cleaned_data.get('password')) # true false
          if user:
              django_login(request,user)
              messages.add_message(request, messages.INFO, "Login oldunuz !!")
              return redirect(next)
          else:
              messages.add_message(request, messages.INFO, "Bele bir istifadeci tapilmadi!")
              
          
             
          
              
              
              
              


    context={
        "form": form,
    }



    return render(request, 'login.html',context)


def register(request, *args, **kwargs):
    form=RegisterForm()
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if  form.is_valid():
           form.save(False)
           
    context={
        "form": form,
    }

    return render(request, 'register.html',context)


def Logout(request):

    django_logout(request)
    return redirect(reverse_lazy("login"))



    