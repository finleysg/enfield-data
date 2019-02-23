from django.contrib import admin
from .models import AccountType, Account, Contact


class ContactInline(admin.TabularInline):
    model = Contact
    verbose_name_plural = "contacts"
    fields = ["last_name", "first_name", "email", "primary_phone", "do_notify", ]
    can_delete = True
    extra = 0


class AccountTypeAdmin(admin.ModelAdmin):
    model = AccountType
    fields = ["description", "tax_rate", "is_active", ]
    list_display = ["description", "tax_rate", "is_active", ]
    list_display_links = ["description", ]


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    save_on_top = True
    fields = ["last_name", "first_name", "email", "primary_phone", "alternate_phone",
              "fax", "do_notify", "notes", ]
    list_display = ["name", "email", "primary_phone", ]
    list_display_links = ("name", )
    search_fields = ["last_name", "first_name", "email", ]


class AccountAdmin(admin.ModelAdmin):
    model = Account
    save_on_top = True
    fields = ["account_type", "account_number", "name", "address", "city", "state", "zip", "notes", ]
    list_display = ["account_type", "account_number", "name", "city", ]
    list_display_links = ("account_number", "name", )
    list_filter = ("account_type", )
    inlines = [ContactInline, ]
    search_fields = ["name", ]


admin.site.register(AccountType, AccountTypeAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Contact, ContactAdmin)
