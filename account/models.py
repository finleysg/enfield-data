from django.db import models
from django.db.models import *
from simple_history.models import HistoricalRecords


class AccountType(models.Model):
    description = models.CharField(verbose_name="Description", max_length=30, default="")
    tax_rate = models.DecimalField(verbose_name="Tax Rate", max_digits=5, decimal_places=4, default=0.0000)
    is_active = models.BooleanField(verbose_name="Active", default=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Account Type'
        verbose_name_plural = 'Account Types'
        ordering = ["description", ]


class Account(models.Model):
    account_type = models.ForeignKey(verbose_name="Account Type", to=AccountType, on_delete=DO_NOTHING)
    account_number = models.CharField(verbose_name="Account Number", max_length=10, unique=True)
    name = models.CharField(verbose_name="Name", max_length=50)
    address = models.CharField(verbose_name="Address", max_length=200, blank=True, null=True)
    city = models.CharField(verbose_name="City", max_length=40, blank=True, null=True)
    state = models.CharField(verbose_name="State", max_length=2, default="TN", blank=True, null=True)
    zip = models.CharField(verbose_name="Zip Code", max_length=10, blank=True, null=True)
    notes = models.TextField(verbose_name="Notes", blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return ["name__icontains", "account_number__icontains", ]

    class Meta:
        ordering = ["account_type__description", "name", ]


class Contact(models.Model):
    account = models.ForeignKey(verbose_name="Account", to=Account, on_delete=CASCADE)
    last_name = models.CharField(verbose_name="Last Name", max_length=30)
    first_name = models.CharField(verbose_name="Last Name", max_length=30)
    email = models.CharField(verbose_name="Email", max_length=200, blank=True, null=True)
    primary_phone = models.CharField(verbose_name="Primary Phone", max_length=20, blank=True, null=True)
    alternate_phone = models.CharField(verbose_name="Alternate Phone", max_length=20, blank=True, null=True)
    fax = models.CharField(verbose_name="Fax", max_length=20, blank=True, null=True)
    do_notify = models.BooleanField(verbose_name="Notification Flag", default=False)
    notes = models.TextField(verbose_name="Notes", blank=True, null=True)
    history = HistoricalRecords()

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return ["last_name__icontains", "first_name__icontains", "email__icontains", ]

    class Meta:
        ordering = ["last_name", "first_name", ]
