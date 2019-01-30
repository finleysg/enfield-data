from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee, User


class EmployeeInline(admin.StackedInline):
    model = Employee
    verbose_name_plural = "employee"
    fields = ["location", "last_name", "first_name", "start_date", "rate", "is_active", "notes", ]
    can_delete = True
    extra = 0


class EnfieldUserAdmin(UserAdmin):
    model = User
    inlines = (EmployeeInline, )
    save_on_top = True


class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    save_on_top = True
    fields = ["location", "last_name", "first_name", "start_date", "rate", "is_active", "notes", ]
    list_display = ["name", "location", "is_active", ]
    list_display_links = ("name", )
    list_filter = ("location", "is_active", )


admin.site.register(User, EnfieldUserAdmin)
admin.site.register(Employee, EmployeeAdmin)
