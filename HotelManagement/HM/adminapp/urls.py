from django.urls import path
from . import views
from .views import feedback

urlpatterns = [

     path("HMhome",views.HMhome,name="HMhome"),
     path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
     path("checkRegistration", views.checkregistration, name="checkregistration"),
     path("changepassword", views.checkChangePassword, name="changepassword"),
     path("logout", views.logout, name="logout"),
     path('search_hotel/', views.search_hotel, name='search_hotel'),
     path('book_hotel', views.book_hotel, name='book_hotel'),
     path('medical_health/', views.medical_health_view, name='medical_health'),
     path('payment_form/',views.process_payment,name='payment_form'),
     path('feedback/', feedback, name='feedback'),


     ]