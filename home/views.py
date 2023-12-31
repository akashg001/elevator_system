from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Elevator, Request
from .serializers import ElevatorSerializer, RequestSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class ElevatorSystem(viewsets.ViewSet):

    @action(detail=True, methods=['GET'])
    def get_elevator_list(self,request):
        queryset = Elevator.objects.all()
        serializer = ElevatorSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def create_elevator(self,request):
        data = request.data
        request_data = data.get('requests')
        serializer = ElevatorSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        elevator = serializer.save()
        if request_data:
            for req in request_data:
                req['elevator'] = elevator.id
            request_serializer = RequestSerializer(data=request_data, many=True)
            request_serializer.is_valid(raise_exception=True)
            request_serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=['PUT'])
    def update_elevator(self,request, elevator_id=None):
        data = request.data
        request_data = data.get('requests')
        elevator = Elevator.objects.get(pk=elevator_id)
        serializer = ElevatorSerializer(instance=elevator, data=data)
        serializer.is_valid(raise_exception=True)
        elevator = serializer.save()
        Request.objects.filter(elevator=elevator).delete()
        if request_data:
            for req in request_data:
                req['elevator'] = elevator.id
            request_serializer = RequestSerializer(data=request_data, many=True)
            request_serializer.is_valid(raise_exception=True)
            request_serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def associate_elevator_with_floor(self,request):
        floor = request.data.get('floor')
        elevators = Elevator.objects.filter(is_available=True, is_operational=True)
        if not elevators:
            return Response({})
        elevator = elevators.first()
        elevator.is_available = False
        elevator.save()
        request_data = [{'floor': floor, 'direction': 'up', 'elevator': elevator.id}]
        request_serializer = RequestSerializer(data=request_data, many=True)
        request_serializer.is_valid(raise_exception=True)
        request_serializer.save()
        serializer = ElevatorSerializer(elevator)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def mark_elevator_available(self,request, elevator_id=None):
        elevator = Elevator.objects.get(pk=elevator_id)
        elevator.is_available = True
        elevator.save()
        return Response({})

    @action(detail=True, methods=['POST'])
    def initialize_elevator_system(self,request):
        num_elevators = request.data.get('num_elevators')
        if num_elevators is None:
            return Response({"error": "Number of elevators is required"}, status=400)
        for _ in range(num_elevators):
            Elevator.objects.create()
        return Response({"message": f"{num_elevators} elevators created"}, status=201)

    @action(detail=True, methods=['GET'])
    def get_available_elevators(self,request):
        elevators = Elevator.objects.filter(is_available=True)
        serializer = ElevatorSerializer(elevators, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def get_non_operational_elevators(self,request):
        elevators = Elevator.objects.filter(is_operational=False)
        serializer = ElevatorSerializer(elevators, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def get_elevator_status(self,request, elevator_id):
        try:
            elevator = Elevator.objects.get(pk=elevator_id)
        except Elevator.DoesNotExist:
            return Response({"error": "Elevator not found"}, status=404)
        serializer = ElevatorSerializer(elevator)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def get_elevator_current_floor(self,request, elevator_id):
        try:
            elevator = Elevator.objects.get(pk=elevator_id)
        except Elevator.DoesNotExist:
            return Response({"error": "Elevator not found"}, status=404)
        return Response({"current_floor": elevator.current_floor})

    @action(detail=True, methods=['GET'])
    def get_request_list(self,request):
        queryset = Request.objects.all()
        serializer = RequestSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def create_request(self,request):
        serializer = RequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request_obj = serializer.save()
        return Response(serializer.data)