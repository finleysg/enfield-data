from django.db import models
from django.db.models import *
from simple_history.models import HistoricalRecords

from account.models import Account, AccountType
from employee.models import Employee, Location


class LaborType(models.Model):
    name = models.CharField(verbose_name="Name", max_length=30)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Labor Type'
        verbose_name_plural = 'Labor Types'
        ordering = ["name", ]


class InvoiceType(models.Model):
    name = models.CharField(verbose_name="Name", max_length=30)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Invoice Type'
        verbose_name_plural = 'Invoice Types'
        ordering = ["name", ]


class ServiceType(models.Model):
    name = models.CharField(verbose_name="Name", max_length=30)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service Type'
        verbose_name_plural = 'Service Types'
        ordering = ["name", ]


class AccountTypeServices(models.Model):
    account_type = models.ForeignKey(verbose_name="Account Type", to=AccountType, on_delete=CASCADE)
    service_type = models.ForeignKey(verbose_name="Service Type", to=ServiceType, on_delete=CASCADE)
    rate = models.DecimalField(verbose_name="Default Rate", max_digits=12, decimal_places=4, default=0)
    estimated_time = models.IntegerField(verbose_name="Default Estimated Time", default=0)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    history = HistoricalRecords()

    def __str__(self):
        return "{} {}".format(self.account_type.description, self.service_type.name)

    class Meta:
        verbose_name = 'Account-Service Mapping'
        verbose_name_plural = 'Account-Service Mapping'
        ordering = ["account_type__name", "service_type__name", ]


class AccountTypeLabor(models.Model):
    account_type_service = models.ForeignKey(verbose_name="Service Type", to=AccountTypeServices, on_delete=CASCADE)
    labor_type = models.ForeignKey(verbose_name="Labor Type", to=LaborType, on_delete=CASCADE)
    rate = models.DecimalField(verbose_name="Default Rate", max_digits=9, decimal_places=4, default=0.0000)
    rate_type = models.CharField(verbose_name="Default Rate Type", max_length=1, default="F")
    history = HistoricalRecords()

    def __str__(self):
        return "{} {}".format(self.account_type_service.service_type.name, self.labor_type.name)

    class Meta:
        verbose_name = 'Service-Labor Mapping'
        verbose_name_plural = 'Service-Labor Mapping'


class Invoice(models.Model):
    invoice_number = models.CharField(verbose_name="Invoice Number", max_length=20)
    location = models.ForeignKey(verbose_name="Location", to=Location, on_delete=DO_NOTHING)
    invoice_type = models.ForeignKey(verbose_name="Invoice Type", to=InvoiceType, on_delete=DO_NOTHING)
    account = models.ForeignKey(verbose_name="Account", to=Account, on_delete=DO_NOTHING)
    receive_date = models.DateField(verbose_name="Received")
    complete_date = models.DateField(verbose_name="Completed", blank=True, null=True)
    year = models.IntegerField(verbose_name="Year", blank=True, null=True)
    make = models.CharField(verbose_name="Make", max_length=20, blank=True, null=True)
    model = models.CharField(verbose_name="Model", max_length=30, blank=True, null=True)
    color = models.CharField(verbose_name="Color", max_length=20, blank=True, null=True)
    vin = models.CharField(verbose_name="VIN", max_length=20, blank=True, null=True)
    stock_number = models.CharField(verbose_name="Stock Number", max_length=20, blank=True, null=True)
    po_number = models.CharField(verbose_name="PO Number", max_length=20, blank=True, null=True)
    is_complete = models.BooleanField(verbose_name="Is Complete", default=False)
    is_paid = models.BooleanField(verbose_name="Is Paid", default=False)
    tax_rate = models.DecimalField(verbose_name="Tax Rate", max_digits=5, decimal_places=4, default=0.0)
    history = HistoricalRecords()

    class Meta:
        ordering = ["-id", ]

    @property
    def vehicle(self):
        return "{} {} {} {}".format(self.year, self.color, self.make, self.model)

    def __str__(self):
        return "{}: {} {}".format(self.invoice_number, self.account.name, self.vehicle)


class Labor(models.Model):
    invoice = models.ForeignKey(verbose_name="Invoice", to=Invoice, on_delete=CASCADE)
    employee = models.ForeignKey(verbose_name="Employee", to=Employee, on_delete=DO_NOTHING)
    labor_type = models.ForeignKey(verbose_name="Labor Type", to=LaborType, on_delete=DO_NOTHING)
    estimated_rate = models.DecimalField(verbose_name="Estimated Rate", max_digits=6, decimal_places=3)
    actual_rate = models.DecimalField(verbose_name="Actual Rate", max_digits=6, decimal_places=3)
    estimated_time = models.IntegerField(verbose_name="Estimated Time")
    actual_time = models.IntegerField(verbose_name="Estimated Time")
    labor_date = models.DateField(verbose_name="Labor Date")
    history = HistoricalRecords()

    def __str__(self):
        return "{}: {} {} {}".format(self.invoice.invoice_number, self.employee.name,
                                     self.labor_type.name, self.labor_date)

    class Meta:
        verbose_name = 'Labor'
        verbose_name_plural = 'Labor'


class Service(models.Model):
    invoice = models.ForeignKey(verbose_name="Invoice", to=Invoice, on_delete=CASCADE)
    service_type = models.ForeignKey(verbose_name="Service Type", to=ServiceType, on_delete=DO_NOTHING)
    rate = models.DecimalField(verbose_name="Rate", max_digits=12, decimal_places=4)
    estimated_time = models.IntegerField(verbose_name="Estimated Time")
    service_date = models.DateField(verbose_name="Service Date")
    history = HistoricalRecords()

    def __str__(self):
        return "{}: {} {}".format(self.invoice.invoice_number, self.service_type.name, self.service_date)

    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Services'


class VehicleLog(models.Model):
    invoice = models.ForeignKey(verbose_name="Invoice", to=Invoice, on_delete=DO_NOTHING)
    stock_number = models.CharField(verbose_name="Stock Number", max_length=20, db_index=True)
    note = models.CharField(verbose_name="Note", max_length=160)
    log_date = models.DateField(verbose_name="Log Date", auto_created=True)

    def __str__(self):
        return "{}: {} ({})".format(self.stock_number, self.invoice.invoice_number, self.log_date)

    class Meta:
        verbose_name = 'Vehicle Log'
        verbose_name_plural = 'Vehicle Log'
        ordering = ["-id", ]
