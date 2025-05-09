
from django.urls import path
from . views import RegisterView,Dashboardview,TranscationView,export_transcation



urlpatterns = [
  
    path('register/',RegisterView.as_view(),name='register'),
    path('',Dashboardview.as_view(),name='dashboard'),
    path('transcation/add',TranscationView.as_view(),name='transcation'),
    path('export/',export_transcation,name='export')
]
