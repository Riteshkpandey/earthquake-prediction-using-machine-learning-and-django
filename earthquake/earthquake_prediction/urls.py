from django.urls import path
from earthquake_prediction import views
from django.views.generic.base import RedirectView
urlpatterns = [
    path('',RedirectView.as_view(url="home/")),
    
    path('home/',views.home),
    path('about/',views.about),
    path('contactus/',views.contactus),
]
