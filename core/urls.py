from django.urls import path
from .views import contact,about,HomeView,ContactView
urlpatterns=[
    path("",HomeView.as_view(),name="home"),
    path("contact-us/",ContactView.as_view(),name="contact"),
    path("about-us/",about,name="about")
]