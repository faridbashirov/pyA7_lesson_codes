from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from acoounts.forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate,login as django_login,logout as django_logout
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
from django.contrib.auth import get_user_model
User=get_user_model()


# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
# https://medium.com/@namantam1/login-with-facebook-and-google-in-django-using-social-auth-app-django-d042bfeb04cb
# https://medium.com/geekculture/django-social-authentication-sign-in-with-facebook-eb52c384e1d

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
            user=form.save(False)
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect(reverse_lazy("login"))
           
    context={
        "form": form,
    }

    return render(request, 'register.html',context)


def Logout(request):

    django_logout(request)
    return redirect(reverse_lazy("login"))


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        django_login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')


    