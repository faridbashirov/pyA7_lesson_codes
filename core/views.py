from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from product.models import Category
from django.utils.translation import gettext as _
from core.forms import ContactForm
from core.models import Contact
from django.contrib import messages
from django.views.generic import TemplateView,CreateView

# def home(request):

#     return render(request,"index.html")

class HomeView(TemplateView):
    template_name ="index.html"

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


class ContactView(CreateView):
    template_name="contact.html"
    form_class=ContactForm
    model=Contact
    success_url=reverse_lazy("contact")

    def get_success_url(self) -> str:
        messages.add_message(self.request, messages.INFO, _("Ugurlu gonderildi!!"))
        return super().get_success_url()

def about(request):
    return render(request,"about.html")




