from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name="index"),
    path('about/', about_view, name="about"),
    path('contact/', contact_view, name="contact"),
    path('booking/', booking_view, name="booking"),
    path('tracking/', tracking_view, name="tracking"),
    path('search_result/', destination_view, name="destination"),
]
