from django.urls import path
from . import views
from .views import generate_text_graphics, bookingAppointment, bookingview, bookingconfirmation, bookingpage

urlpatterns = [
   path('', views.home, name = "home"),
   path('booking/', generate_text_graphics, name = 'generate_text_graphics'),
   path('booking2/', bookingAppointment, name = 'bookingAppointment'),
   path('bookingengraving/', bookingview, name = 'bookingview'),
   path('bookingconfirmation/', bookingconfirmation, name = 'bookingconfirmation'),
   path('bookingpage/', bookingpage, name = 'bookingpage'),


]