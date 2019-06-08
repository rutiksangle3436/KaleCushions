from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
	#home page
    path('', views.index, name='index'),
    
    path('contactus/', views.contactus, name='contactus'),
]
