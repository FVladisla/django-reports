from django.contrib import admin
from .models import Employee, PayrollReport, WorkTimeRecord, ShipmentRevenue, Tariff, TaxesReport

@admin.register(Employee)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(PayrollReport)
class AuthorAdmin(admin.ModelAdmin):
    pass
@admin.register(WorkTimeRecord)
class AuthorAdmin(admin.ModelAdmin):
    pass
@admin.register(ShipmentRevenue)
class AuthorAdmin(admin.ModelAdmin):
    pass
@admin.register(Tariff)
class AuthorAdmin(admin.ModelAdmin):
    pass
@admin.register(TaxesReport)
class AuthorAdmin(admin.ModelAdmin):
    pass