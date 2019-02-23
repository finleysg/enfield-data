from django.contrib import admin
from .models import LaborType, InvoiceType, ServiceType, AccountTypeLabor, AccountTypeServices, Invoice, Labor, Service, \
    VehicleLog


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


class AccountTypeLaborInline(admin.TabularInline):
    model = AccountTypeLabor
    verbose_name_plural = "labor types"
    fields = ["labor_type", "rate", "rate_type", ]
    can_delete = True
    extra = 0


class AccountTypeServicesAdmin(admin.ModelAdmin):
    model = AccountTypeServices
    save_on_top = True
    fields = ["account_type", "service_type", "rate", "is_active", ]
    inlines = [AccountTypeLaborInline, ]
    list_display = ["account_type", "service_type", "rate", "is_active", ]
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
    list_display = ["invoice_number", "location", "account", "receive_date", "vehicle",
                    "stock_number", "vin", "po_number", "is_paid", ]
    list_editable = ["po_number", "is_paid", ]
    list_display_links = ("invoice_number", )
    list_filter = ("location", "receive_date", "account", "is_complete", "is_paid", )
    inlines = [ServiceInline, LaborInline, ]
    search_fields = ["invoice_number", "vin", "stock_number", ]


class VehicleLogAdmin(admin.ModelAdmin):
    model = VehicleLog
    readonly_fields = ["invoice", "stock_number", "note", "log_date", ]
    list_display = ["invoice", "stock_number", "note", "log_date", ]
    list_display_links = None
    list_filter = ("log_date", )
    search_fields = ["invoice__invoice_number", "stock_number", ]


admin.site.register(LaborType, LaborTypeAdmin)
admin.site.register(InvoiceType, InvoiceTypeAdmin)
admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(AccountTypeServices, AccountTypeServicesAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(VehicleLog, VehicleLogAdmin)
