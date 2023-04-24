# เลขาของห้อง myapp
from django.urls import path
from .views import Homepage

urlpatterns = [
    path('',Homepage),
    
]