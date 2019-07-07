from django.urls import path
from  Blog import views as Blog_views

urlpatterns =[
    path('',Blog_views.home,name='blog-home'),
    path('view_form/',Blog_views.view_form,name='view_Form'),
]
