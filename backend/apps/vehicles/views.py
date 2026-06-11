from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Vehicle, VehicleService, FuelLog, TyreRecord, AccidentRecord
from .serializers import VehicleSerializer, VehicleServiceSerializer, FuelLogSerializer, TyreRecordSerializer, AccidentRecordSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    """ViewSet for vehicle management"""
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['vehicle_type', 'status', 'assigned_driver', 'department']
    search_fields = ['registration_number', 'chassis_number', 'make', 'model']
    ordering_fields = ['registration_number', 'acquisition_date']
    
    @action(detail=True, methods=['post'])
    def record_service(self, request, pk=None):
        """Record vehicle service"""
        vehicle = self.get_object()
        serializer = VehicleServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(vehicle=vehicle, created_by=request.user)
            vehicle.current_odometer = request.data.get('odometer_reading', vehicle.current_odometer)
            vehicle.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'])
    def record_fuel(self, request, pk=None):
        """Record fuel consumption"""
        vehicle = self.get_object()
        serializer = FuelLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(vehicle=vehicle, recorded_by=request.user)
            vehicle.current_odometer = request.data.get('odometer_reading', vehicle.current_odometer)
            vehicle.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'])
    def record_accident(self, request, pk=None):
        """Record vehicle accident"""
        vehicle = self.get_object()
        serializer = AccidentRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(vehicle=vehicle, reported_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'])
    def fuel_efficiency(self, request, pk=None):
        """Calculate fuel efficiency"""
        vehicle = self.get_object()
        logs = vehicle.fuel_logs.all().order_by('-log_date')
        
        if len(logs) < 2:
            return Response({'message': 'Not enough fuel logs for efficiency calculation'})
        
        total_fuel = sum(log.fuel_amount for log in logs)
        total_distance = logs[0].odometer_reading - logs[len(logs)-1].odometer_reading
        efficiency = total_distance / total_fuel if total_fuel > 0 else 0
        
        return Response({
            'total_fuel': total_fuel,
            'total_distance': total_distance,
            'fuel_efficiency': round(efficiency, 2)
        })
    
    @action(detail=True, methods=['get'])
    def maintenance_history(self, request, pk=None):
        """Get complete maintenance history"""
        vehicle = self.get_object()
        return Response({
            'services': VehicleServiceSerializer(vehicle.services.all(), many=True).data,
            'fuel_logs': FuelLogSerializer(vehicle.fuel_logs.all(), many=True).data,
            'accidents': AccidentRecordSerializer(vehicle.accidents.all(), many=True).data,
        })


class VehicleServiceViewSet(viewsets.ModelViewSet):
    """ViewSet for vehicle services"""
    queryset = VehicleService.objects.all()
    serializer_class = VehicleServiceSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['vehicle', 'service_type']
    ordering = ['-service_date']


class FuelLogViewSet(viewsets.ModelViewSet):
    """ViewSet for fuel logs"""
    queryset = FuelLog.objects.all()
    serializer_class = FuelLogSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['vehicle']
    ordering = ['-log_date']


class TyreRecordViewSet(viewsets.ModelViewSet):
    """ViewSet for tyre records"""
    queryset = TyreRecord.objects.all()
    serializer_class = TyreRecordSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['vehicle', 'position']


class AccidentRecordViewSet(viewsets.ModelViewSet):
    """ViewSet for accident records"""
    queryset = AccidentRecord.objects.all()
    serializer_class = AccidentRecordSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['vehicle', 'severity', 'insurance_claim']
    ordering = ['-accident_date']
