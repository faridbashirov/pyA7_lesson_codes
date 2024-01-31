from django.urls import path
from .views import home,contact,about
urlpatterns=[
    path("",home,name="home"),
    path("contact-us/",contact,name="contact"),
    path("about-us/",about,name="about")
]