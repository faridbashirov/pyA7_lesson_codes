from django.urls import path,re_path
from .views import login,register,Logout,activate

urlpatterns=[
    path("login/",login,name="login"),
    path("register/",register,name="register"),
    path("logout/",Logout,name="logout"),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
        activate, name='activate'),

]