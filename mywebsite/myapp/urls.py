# เลขาของห้อง myapp
from django.urls import path
# from .views import Homepage,About
from .views import *

urlpatterns = [
    path('',Homepage,name='home-page'),
    path('about/',About,name='about-page'),
    path('services/',Services,name='service-page'),
    path('products/',Products,name='products-page'),
    path('contact/',Contact,name='contact-page'),
    
]