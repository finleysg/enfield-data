from rest_framework import serializers

from account.serializers import AccountSerializer
from employee.serializers import LocationSerializer, EmployeeSerializer
from invoice.models import *


class LaborTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaborType
        fields = ("id", "name", )


class InvoiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceType
        fields = ("id", "name", )


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ("id", "name", )


class AccountTypeServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountTypeServices
        fields = ("id", "account_type", "service_type", "rate", "estimated_time", "is_active", )


class AccountTypeLaborSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountTypeLabor
        fields = ("id", "account_type_service", "labor_type", "rate", "rate_type", )


class LaborSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    labor_type = LaborTypeSerializer()

    class Meta:
        model = Labor
        fields = ("id", "invoice", "employee", "labor_type", "estimated_rate", "actual_rate", "estimated_time",
                  "actual_time", "labor_date", )


class ServiceSerializer(serializers.ModelSerializer):
    service_type = ServiceTypeSerializer()

    class Meta:
        model = Service
        fields = ("id", "invoice", "service_type", "rate", "estimated_time", "service_date", )


class VehicleLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleLog
        fields = ("id", "invoice", "stock_number", "note", "log_date", )


class InvoiceSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    invoice_type = InvoiceTypeSerializer()
    account = AccountSerializer()
    labor = LaborSerializer(many=True, required=False)
    services = ServiceSerializer(many=True, required=False)
    history = VehicleLogSerializer(many=True, required=False)

    class Meta:
        model = Invoice
        fields = ("id", "invoice_number", "location", "invoice_type", "account", "receive_date", "complete_date",
                  "year", "make", "model", "color", "vin", "stock_number", "po_number", "is_complete", "is_paid",
                  "tax_rate", "labor", "services", "history", )


class SimpleInvoiceSerializer(serializers.ModelSerializer):
    location = serializers.CharField(source="location.name")
    invoice_type = serializers.CharField(source="invoice_type.name")
    account = serializers.CharField(source="account.name")

    class Meta:
        model = Invoice
        fields = ("id", "invoice_number", "location", "invoice_type", "account", "receive_date", "complete_date",
                  "year", "make", "model", "color", "vin", "stock_number", "po_number", "is_complete", "is_paid", )
