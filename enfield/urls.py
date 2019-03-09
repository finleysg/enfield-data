"""enfield-data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from rest_framework.routers import DefaultRouter

from account import views as account_views
from employee import views as employee_views
from invoice import views as invoice_views

admin.site.site_header = "Enfield Detail Administration"

router = DefaultRouter()
router.register(r"account-types", account_views.AccountTypeViewSet, "account-types")
router.register(r"accounts", account_views.AccountViewSet, "accounts")
router.register(r"contacts", account_views.ContactViewSet, "contacts")
router.register(r"employees", employee_views.EmployeeViewSet, "employees")
router.register(r"employee-logs", employee_views.EmployeeLogViewSet, "employee-logs")
router.register(r"locations", employee_views.LocationViewSet, "locations")
router.register(r"account-type-labor", invoice_views.AccountTypeLaborViewSet, "account-type-labor")
router.register(r"account-type-services", invoice_views.AccountTypeServicesViewSet, "account-type-services")
router.register(r"invoice-type", invoice_views.InvoiceTypeViewSet, "invoice-type")
router.register(r"invoice", invoice_views.InvoiceViewSet, "invoice")
router.register(r"labor", invoice_views.LaborViewSet, "labor")
router.register(r"labor-type", invoice_views.LaborTypeViewSet, "labor-type")
router.register(r"service", invoice_views.ServiceViewSet, "service")
router.register(r"service-type", invoice_views.ServiceTypeViewSet, "service-type")
router.register(r"vehicle-log", invoice_views.VehicleLogViewSet, "vehicle-log")

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^api/", include(router.urls)),
    url(r"^api/vehicle-search/(?P<vin>[\w]+)/$", invoice_views.vehicle_search),
    url(r"^grappelli/", include("grappelli.urls")),
    url(r'^report_builder/', include('report_builder.urls')),
]
