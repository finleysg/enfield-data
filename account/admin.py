from django.contrib import admin
from .models import AccountType, Account, ContactType, Contact


class ContactInline(admin.StackedInline):
    model = Contact
    verbose_name_plural = "contacts"
    fields = ["contact_type", "last_name", "first_name", "email", "primary_phone", "alternative_phone",
              "fax", "do_notify", "notes", ]
    can_delete = True
    extra = 0


class AccountTypeAdmin(admin.ModelAdmin):
    model = AccountType
    fields = ["name", ]
    list_display = ["name", ]
    list_display_links = ["name", ]


class ContactTypeAdmin(admin.ModelAdmin):
    model = ContactType
    fields = ["name", ]
    list_display = ["name", ]
    list_display_links = ["name", ]


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    save_on_top = True
    fields = ["contact_type", "last_name", "first_name", "email", "primary_phone", "alternative_phone",
              "fax", "do_notify", "notes", ]
    list_display = ["name", "email", "primary_phone", "contact_type", ]
    list_display_links = ("name", )
    list_filter = ("contact_type", "do_notify", )


class AccountAdmin(admin.ModelAdmin):
    model = Account
    save_on_top = True
    fields = ["account_type", "account_number", "name", "address", "city", "state", "zip", "notes", ]
    list_display = ["account_type", "account_number", "name", "city", ]
    list_display_links = ("account_number", "name", )
    list_filter = ("account_type", )
    inlines = [ContactInline, ]


admin.site.register(AccountType, AccountTypeAdmin)
admin.site.register(ContactType, ContactTypeAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Contact, ContactAdmin)
