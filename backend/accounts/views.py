from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from datetime import date
from rest_framework.permissions import AllowAny


from .models import Profile, Appointment
from .serializers import RegisterSerializer, AppointmentSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

# Ensure CSRF token is set in the frontend
@ensure_csrf_cookie
def csrf_token_view(request):
    return JsonResponse({'message': 'CSRF token set'})

# Register View to handle user registration
@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # Create the user first
            user = serializer.save()
            # Set the role
            role = request.data.get("role", "patient")
            
            # Try to get or create the profile for this user
            profile, created = Profile.objects.get_or_create(user=user, role=role)
            
            # Log the result to confirm it's being created
            print(f"Profile created: {profile} | Created: {created}")
            
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Login View to authenticate user and retrieve their role
@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            try:
                profile = Profile.objects.get(user=user)
                print(f"Profile found: {profile}")
                
                login(request, user)  # ✅ Important: This sets the session!
                
                return Response({
                    "message": "Login successful",
                    "role": profile.role,
                    "username": user.username
                }, status=status.HTTP_200_OK)
            except Profile.DoesNotExist:
                return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)



# Get all doctors available in the system
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_doctors(request):
    doctors = Profile.objects.filter(role='doctor').select_related('user')
    doctor_data = [{'id': d.user.id, 'username': d.user.username} for d in doctors]
    return Response(doctor_data)

# Book an appointment for the patient (logged-in user)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_appointment(request):
    data = request.data.copy()
    data['patient'] = request.user.id  # Automatically assign the logged-in user as the patient
    serializer = AppointmentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Appointment booked successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get all appointments for the logged-in doctor
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def doctor_appointments(request):
    user = request.user
    print("🔍 Logged-in user:", user.username)

    try:
        profile = Profile.objects.get(user=user)
        print("✅ Profile found:", profile)

        if profile.role != 'doctor':
            return Response({"error": "Access denied"}, status=403)

    except Profile.DoesNotExist:
        print("❌ Profile not found for:", user.username)
        return Response({"error": "Profile not found"}, status=404)

    appointments = Appointment.objects.filter(doctor=user).select_related('patient')

    data = [
        {
            "patient": appt.patient.username,
            "date": appt.date,
            "time": appt.time.strftime('%H:%M')
        } for appt in appointments
    ]
    return Response(data)



# Get all appointments for the logged-in patient
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_appointments(request):
    user = request.user
    appointments = Appointment.objects.filter(patient=user).select_related('doctor')
    data = [
        {
            'id': appt.id,
            'date': appt.date,
            'time': appt.time,
            'doctor_name': appt.doctor.username
        } for appt in appointments
    ]
    return Response(data)
