
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.ask,name='contact'),
    path('about', views.about, name='about'),

    path('signup',views.handleSignup,name='signup'),
    path('login',views.handlelogin,name='login'),
    path('logout',views.handlelogout,name='logout'),




]