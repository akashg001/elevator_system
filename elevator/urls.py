"""
URL configuration for elevator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from home.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path('elevators/', ElevatorSystem.as_view({'get':'get_elevator_list'}), name='get_elevator_list'),
    path('elevators/create/', ElevatorSystem.as_view({'post':'create_elevator'}), name='create_elevator'),
    path('elevators/update/<int:elevator_id>/', ElevatorSystem.as_view({'put':'update_elevator'}), name='update_elevator'),
    path('elevators/associate_with_floor/', ElevatorSystem.as_view({'post':'associate_elevator_with_floor'}), name='associate_elevator_with_floor'),
    path('elevators/mark_available/<int:elevator_id>/', ElevatorSystem.as_view({'post':'mark_elevator_available'}), name='mark_elevator_available'),
    path('elevators/initialize/', ElevatorSystem.as_view({'post':'initialize_elevator_system'}), name='initialize_elevator_system'),
    path('elevators/available/', ElevatorSystem.as_view({'get':'get_available_elevators'}), name='get_available_elevators'),
    path('elevators/non_operational/', ElevatorSystem.as_view({'get':'get_non_operational_elevators'}), name='get_non_operational_elevators'),
    path('elevators/status/<int:elevator_id>/', ElevatorSystem.as_view({'get':'get_elevator_status'}), name='get_elevator_status'),
    path('elevators/current_floor/<int:elevator_id>/', ElevatorSystem.as_view({'get':'get_elevator_current_floor'}), name='get_elevator_current_floor'),
    path('requests/', ElevatorSystem.as_view({'get':'get_request_list'}), name='get_request_list'),
    path('requests/create/', ElevatorSystem.as_view({'post':'create_request'}), name='create_request'),
]
