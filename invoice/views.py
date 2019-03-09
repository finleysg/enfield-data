from datetime import date

from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import InvoiceType, Invoice, LaborType, Labor, ServiceType, \
    Service, AccountTypeLabor, AccountTypeServices, VehicleLog
from .serializers import InvoiceTypeSerializer, InvoiceSerializer, \
    LaborTypeSerializer, LaborSerializer, ServiceTypeSerializer, \
    ServiceSerializer, AccountTypeLaborSerializer, AccountTypeServicesSerializer, \
    VehicleLogSerializer, SimpleInvoiceSerializer
from .vin import search_by_vin


class InvoiceTypeViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceTypeSerializer
    queryset = InvoiceType.objects.all()


class LaborTypeViewSet(viewsets.ModelViewSet):
    serializer_class = LaborTypeSerializer
    queryset = LaborType.objects.all()


class ServiceTypeViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()


class AccountTypeLaborViewSet(viewsets.ModelViewSet):
    serializer_class = AccountTypeLaborSerializer

    def get_queryset(self):
        queryset = AccountTypeLabor.objects.all()
        service_type = self.request.query_params.get("service_type", None)
        if service_type is not None:
            queryset = queryset.filter(account_type_service=service_type)
        return queryset


class AccountTypeServicesViewSet(viewsets.ModelViewSet):
    serializer_class = AccountTypeServicesSerializer

    def get_queryset(self):
        queryset = AccountTypeServices.objects.all()
        queryset = queryset.filter(is_active=True)
        account_type = self.request.query_params.get("account_type", None)
        if account_type is not None:
            queryset = queryset.filter(account_type=account_type)
        return queryset


class LaborViewSet(viewsets.ModelViewSet):
    serializer_class = LaborSerializer
    queryset = Labor.objects.all()


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        queryset = Invoice.objects.all()
        in_shop = self.request.query_params.get("in_shop", None)
        completed_today = self.request.query_params.get("completed_today", None)

        if in_shop is not None:
            queryset = queryset.filter(is_complete=False)
        if completed_today is not None:
            today = date.today()
            queryset = queryset.filter(complete_date=today)

        return queryset


class VehicleLogViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleLogSerializer
    queryset = VehicleLog.objects.all()


@api_view(("GET",))
@permission_classes((permissions.AllowAny,))
def vehicle_search(request, vin):
    nhtsa = search_by_vin(vin)
    by_vin = list(Invoice.objects.all().filter(vin__istartswith=vin[:8]))
    by_sn = list(Invoice.objects.all().filter(stock_number__istartswith=vin[:8]))

    s1 = SimpleInvoiceSerializer(by_vin, many=True, context={"request": request})
    s2 = SimpleInvoiceSerializer(by_sn, many=True, context={"request": request})
    return Response({
        "nhtsa": nhtsa,
        "vin_search": s1.data,
        "stock_number_search": s2.data
    })
