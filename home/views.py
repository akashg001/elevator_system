from rest_framework import viewsets
from .models import Elevator, Request
from .serializers import ElevatorSerializer, RequestSerializer

class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    def perform_create(self, serializer):
        request_data = self.request.data.get('requests')
        elevator = serializer.save()
        if request_data:
            for request in request_data:
                request['elevator'] = elevator.id
            request_serializer = RequestSerializer(data=request_data, many=True)
            request_serializer.is_valid(raise_exception=True)
            request_serializer.save()

    def perform_update(self, serializer):
        request_data = self.request.data.get('requests')
        elevator = serializer.save()
        if request_data:
            Request.objects.filter(elevator=elevator).delete()
            for request in request_data:
                request['elevator'] = elevator.id
            request_serializer = RequestSerializer(data=request_data, many=True)
            request_serializer.is_valid(raise_exception=True)
            request_serializer.save()

    def associate_elevator_with_floor(self, floor):
        elevators = self.queryset.filter(is_available=True, is_operational=True)
        if not elevators:
            return None
        elevator = elevators.first()
        elevator.is_available = False
        elevator.save()
        request_data = [{'floor': floor, 'direction': 'up', 'elevator': elevator.id}]
        request_serializer = RequestSerializer(data=request_data, many=True)
        request_serializer.is_valid(raise_exception=True)
        request_serializer.save()
        return elevator

    def mark_elevator_available(self, elevator_id):
        elevator = self.queryset.get(pk=elevator_id)
        elevator.is_available = True
        elevator.save()

    def assign_elevator(self, floor, direction):
        elevators = self.queryset.filter(is_available=True, is_operational=True)
        if not elevators:
            return None

        # Find the closest available elevator to the requested floor
        closest_elevator = None
        min_distance = float('inf')

        for elevator in elevators:
            distance = abs(elevator.current_floor - floor)
            if distance < min_distance:
                min_distance = distance
                closest_elevator = elevator

        if closest_elevator:
            closest_elevator.is_available = False
            closest_elevator.save()
            request_data = [{'floor': floor, 'direction': direction, 'elevator': closest_elevator.id}]
            request_serializer = RequestSerializer(data=request_data, many=True)
            request_serializer.is_valid(raise_exception=True)
            request_serializer.save()

        return closest_elevator
