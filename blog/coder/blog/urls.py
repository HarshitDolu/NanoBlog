from . import views
from django.urls import path,include

urlpatterns = [
    path('postcomment', views.postcomment, name='postcomment'),
    path('',views.blogHome,name='blogHome'),
    path('<str:slug>',views.blogPost,name='blogPost'),



]