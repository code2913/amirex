from django.urls import path
from . import views

urlpatterns = [
    path('',views.Homepage.as_view(),name="home"),
    path('contact-us/',views.Contact.as_view(),name="contact")
]