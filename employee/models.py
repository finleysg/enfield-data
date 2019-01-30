from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import *
from simple_history.models import HistoricalRecords


class User(AbstractUser):
    pass


class Location(models.Model):
    name = models.CharField(verbose_name="Name", max_length=30)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name", ]


class Employee(models.Model):
    location = models.ForeignKey(verbose_name="Location", to=Location, on_delete=DO_NOTHING)
    user = models.ForeignKey(verbose_name="User", to=User, null=True, blank=True, on_delete=DO_NOTHING)
    last_name = models.CharField(verbose_name="Last Name", max_length=30)
    first_name = models.CharField(verbose_name="First Name", max_length=30)
    start_date = models.DateField(verbose_name="Start Date", null=True, blank=True)
    rate = models.DecimalField(verbose_name="Rate", max_digits=4, decimal_places=3, default=1.0)
    is_active = models.BooleanField(verbose_name="Currently Employed", default=True)
    notes = models.TextField(verbose_name="Notes", blank=True, null=True)
    history = HistoricalRecords()

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["last_name", "first_name", ]


class EmployeeLog(models.Model):
    location = models.ForeignKey(verbose_name="Location", to=Location, on_delete=DO_NOTHING)
    employee = models.ForeignKey(verbose_name="Employee", to=Employee, on_delete=DO_NOTHING)
    sign_in_date = models.DateTimeField(verbose_name="Signed In", auto_now_add=True)
    sign_out_date = models.DateTimeField(verbose_name="Signed Out", blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return "{} {} {}".format(self.employee.name, self.location.name, self.sign_in_date)

    class Meta:
        ordering = ["sign_in_date", ]
