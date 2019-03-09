from rest_framework import serializers

from .models import *


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("id", "name", )


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "location", "user", "last_name", "first_name", "start_date", "rate", "is_active", "notes", )


class EmployeeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeLog
        fields = ("id", "location", "employee", "sign_in_date", "sign_out_date", )
