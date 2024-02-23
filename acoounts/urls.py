from django.urls import path
from .views import login,register,Logout

urlpatterns=[
    path("login/",login,name="login"),
    path("register/",register,name="register"),
    path("logout/",Logout,name="logout"),

]