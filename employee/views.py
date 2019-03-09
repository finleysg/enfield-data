from rest_framework import viewsets

from .models import Employee, EmployeeLog, Location
from .serializers import EmployeeSerializer, EmployeeLogSerializer, LocationSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        queryset = queryset.filter(is_active=True)
        return queryset


class EmployeeLogViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeLogSerializer
    queryset = EmployeeLog.objects.all()


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
