from django.urls import path
from auth import views
from django.contrib.auth import views as auth_view

urlpatterns = [
  path('login/', views.Login.as_view(), name='login'),
  path('logout/', views.Logout.as_view(), name='logout'),
  path('signup/', views.Signup.as_view(), name='signup'),
  path('contactus/', views.ContactUs.as_view(), name='contactus'),
]