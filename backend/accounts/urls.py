from django.urls import path
from .views import RegisterView, LoginView, get_doctors, book_appointment, doctor_appointments, csrf_token_view, my_appointments

urlpatterns = [
    path('csrf/', csrf_token_view),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'), 
    path('doctors/', get_doctors, name='get_doctors'),
    path('appointments/book/', book_appointment, name='book_appointment'),
    path('doctor-appointments/', doctor_appointments, name='doctor_appointments'),
    path('appointments/mine/', my_appointments),
]
