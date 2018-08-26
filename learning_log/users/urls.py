"""set users model"""
from django.urls import path,re_path
from django.contrib.auth import views as auth_views

from . import views

app_name='users'
urlpatterns = [
    # login page
    re_path(r'^login/$',auth_views.LoginView.as_view(template_name='users/login.html'),
           name='login'),
    #login out
    re_path(r'^loginout/$',views.logout_view,name='logout'),
    #register
    re_path(r'^register$',views.register,name='register'),
]
