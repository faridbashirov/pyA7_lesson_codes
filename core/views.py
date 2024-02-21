from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from product.models import Category
from core.forms import ContactForm
from django.contrib import messages

def home(request):

    return render(request,"index.html")

def contact(request):
    form=ContactForm()
  
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Ugurlu gonderildi!!")

            return redirect(reverse_lazy("home"))

    context={
        "form": form,
    }
    

    return render(request,"contact.html",context)


def about(request):
    return render(request,"about.html")




