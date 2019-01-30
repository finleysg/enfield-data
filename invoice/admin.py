from django.contrib import admin
from .models import LaborType, InvoiceType, ServiceType, AccountTypeLabor, AccountTypeServices, Invoice, Labor, Service


class LaborInline(admin.TabularInline):
    model = Labor
    verbose_name_plural = "labor"
    fields = ["labor_type", "employee", "actual_rate", "actual_time", "labor_date", ]
    can_delete = True
    extra = 0


class ServiceInline(admin.TabularInline):
    model = Service
    verbose_name_plural = "services"
    fields = ["service_type", "rate", "estimated_time", "service_date", ]
    can_delete = True
    extra = 0


class LaborTypeAdmin(admin.ModelAdmin):
    model = LaborType
    fields = ["name", ]
    list_display = ["name", ]
    list_display_links = ["name", ]


class InvoiceTypeAdmin(admin.ModelAdmin):
    model = InvoiceType
    fields = ["name", ]
    list_display = ["name", ]
    list_display_links = ["name", ]


class ServiceTypeAdmin(admin.ModelAdmin):
    model = ServiceType
    fields = ["name", ]
    list_display = ["name", ]
    list_display_links = ["name", ]


class AccountTypeLaborAdmin(admin.ModelAdmin):
    model = AccountTypeLabor
    save_on_top = True
    fields = ["account_type", "labor_type", "rate", "estimated_time", "is_active", ]
    list_display = ["account_type", "labor_type", "rate", "estimated_time", "is_active", ]
    list_display_links = ("account_type", "labor_type", )
    list_filter = ("account_type", "labor_type", "is_active", )


class AccountTypeServicesAdmin(admin.ModelAdmin):
    model = AccountTypeServices
    save_on_top = True
    fields = ["account_type", "service_type", "rate", "estimated_time", "is_active", ]
    list_display = ["account_type", "service_type", "rate", "estimated_time", "is_active", ]
    list_display_links = ("account_type", "service_type", )
    list_filter = ("account_type", "service_type", "is_active", )


class InvoiceAdmin(admin.ModelAdmin):
    model = Invoice
    save_on_top = True
    # readonly_fields = ["invoice_number", ]
    fieldsets = (
        ("", {
            # "readonly_fields": ("invoice_number", ),
            "fields": (("invoice_number", "invoice_type", ),
                       ("location", "account", ), ("receive_date", "complete_date", ), )
        }),
        ("Vehicle", {
            "fields": (("year", "color", ), ("make", "model", ), ("vin", "stock_number", ), )
        }),
        ("Payment", {
            "fields":  ("po_number", "is_complete", "is_paid", "tax_rate", ),
        }),
    )
    list_display = ["invoice_number", "location", "account", "receive_date", "vehicle", ]
    list_display_links = ("invoice_number", )
    list_filter = ("location", "receive_date", "is_complete", "is_paid", )
    inlines = [ServiceInline, LaborInline, ]


admin.site.register(LaborType, LaborTypeAdmin)
admin.site.register(InvoiceType, InvoiceTypeAdmin)
admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(AccountTypeLabor, AccountTypeLaborAdmin)
admin.site.register(AccountTypeServices, AccountTypeServicesAdmin)
admin.site.register(Invoice, InvoiceAdmin)
